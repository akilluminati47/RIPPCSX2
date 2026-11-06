// SPDX-FileCopyrightText: 2002-2026 PCSX2 Dev Team
// SPDX-License-Identifier: GPL-3.0+

#include "RIPART.h"

#include "pcsx2/Config.h"

#include "common/Path.h"
#ifdef _WIN32
#include "common/RedtapeWindows.h"
#endif

#include <QtCore/QDir>
#include <QtCore/QFile>
#include <QtCore/QFileInfo>
#include <QtCore/QHash>
#include <QtCore/QMetaObject>
#include <QtCore/QRandomGenerator>
#include <QtCore/QRegularExpression>
#include <QtCore/QSet>
#include <QtCore/QTimer>
#include <QtGui/QIcon>
#include <QtGui/QPixmap>
#include <QtWidgets/QAbstractItemView>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFileDialog>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMessageBox>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QVBoxLayout>

#include <algorithm>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <cstring>
#include <cwchar>
#include <functional>
#include <initializer_list>
#include <iterator>
#include <memory>
#include <mutex>
#include <string>
#include <thread>
#include <utility>
#include <vector>

#ifdef _WIN32
#include <winhttp.h>
#pragma comment(lib, "winhttp.lib")
#else
#include <curl/curl.h>
#endif

namespace
{
	// danielb7390's monthly backup of OPL Manager's database, on archive.org: one uncompressed zip, so any piece of art is a
	// byte range, and the zip's directory (8.6 MB) is the whole list. The numbers are this backup's, read from its end record.
#ifdef _WIN32
	const wchar_t* const BACKUP_HOST = L"archive.org";
	const wchar_t* const BACKUP_PATH = L"/download/OPLM_ART_2024_09/OPLM_ART_2024_09.zip";
#else
	const char* const BACKUP_URL = "https://archive.org/download/OPLM_ART_2024_09/OPLM_ART_2024_09.zip";
#endif
	constexpr u64 BACKUP_DIR_OFFSET = 5530939920ull;
	constexpr u64 BACKUP_DIR_SIZE = 8623924ull;
	const char* const CACHE_DIR = "ripart";
	const char* const CACHE_NAME = "OPLM_ART_2024_09";

	constexpr int DECOY_BYTES = 2048;

#ifdef _WIN32
	/// One connection to the backup, on the thread that made it. Asks for one range at a time.
	class Net
	{
	public:
		explicit Net(std::atomic<bool>* cancel)
			: m_cancel(cancel)
		{
			m_session = WinHttpOpen(L"RIPART/1.0", WINHTTP_ACCESS_TYPE_AUTOMATIC_PROXY, WINHTTP_NO_PROXY_NAME, WINHTTP_NO_PROXY_BYPASS, 0);
			if (m_session)
				WinHttpSetTimeouts(m_session, 10000, 15000, 20000, 20000);
			useBase();
		}

		~Net()
		{
			if (m_connect)
				WinHttpCloseHandle(m_connect);
			if (m_session)
				WinHttpCloseHandle(m_session);
		}

		Net(const Net&) = delete;
		Net& operator=(const Net&) = delete;

		/// The bytes from `from` to `to`, inclusive. Tries again on a server's error: archive.org's nodes answer 500 now and then.
		bool range(u64 from, u64 to, QByteArray* out)
		{
			for (int attempt = 0; attempt < 6; attempt++)
			{
				if (m_cancel->load())
					return false;
				if (rangeOnce(from, to, out))
					return true;
				useBase(); // the storage node may be what failed: ask for a new one
				for (int waited = 0; waited < 1000 + attempt * 1500 && !m_cancel->load(); waited += 100)
					std::this_thread::sleep_for(std::chrono::milliseconds(100));
			}
			return false;
		}

	private:
		void connectTo(const std::wstring& host, const std::wstring& path)
		{
			if (m_connect)
				WinHttpCloseHandle(m_connect);
			m_connect = m_session ? WinHttpConnect(m_session, host.c_str(), INTERNET_DEFAULT_HTTPS_PORT, 0) : nullptr;
			m_path = path;
		}

		void useBase()
		{
			m_host.clear();
			connectTo(BACKUP_HOST, BACKUP_PATH);
		}

		// where the redirect landed, so the next range goes straight there. Only ever one of archive.org's own hosts
		void followRedirect(HINTERNET request)
		{
			DWORD size = 0;
			WinHttpQueryOption(request, WINHTTP_OPTION_URL, nullptr, &size);
			if (size == 0)
				return;
			std::wstring url(size / sizeof(wchar_t), L'\0');
			if (!WinHttpQueryOption(request, WINHTTP_OPTION_URL, url.data(), &size))
				return;
			url.resize(wcsnlen(url.c_str(), url.size()));

			wchar_t host[256], path[1024];
			URL_COMPONENTS parts = {};
			parts.dwStructSize = sizeof(parts);
			parts.lpszHostName = host;
			parts.dwHostNameLength = static_cast<DWORD>(std::size(host));
			parts.lpszUrlPath = path;
			parts.dwUrlPathLength = static_cast<DWORD>(std::size(path));
			if (!WinHttpCrackUrl(url.c_str(), 0, 0, &parts) || parts.nScheme != INTERNET_SCHEME_HTTPS)
				return;
			const std::wstring name(host);
			const std::wstring tail(L".archive.org");
			if (name.size() > tail.size() && name.compare(name.size() - tail.size(), tail.size(), tail) == 0 && name != m_host)
			{
				m_host = name;
				connectTo(name, path);
			}
		}

		bool rangeOnce(u64 from, u64 to, QByteArray* out)
		{
			if (!m_connect)
				return false;
			HINTERNET request = WinHttpOpenRequest(m_connect, L"GET", m_path.c_str(), nullptr, WINHTTP_NO_REFERER,
				WINHTTP_DEFAULT_ACCEPT_TYPES, WINHTTP_FLAG_SECURE);
			if (!request)
				return false;

			const std::wstring header = L"Range: bytes=" + std::to_wstring(from) + L"-" + std::to_wstring(to) + L"\r\n";
			DWORD status = 0, statusSize = sizeof(status);
			bool ok = WinHttpSendRequest(request, header.c_str(), static_cast<DWORD>(header.size()), WINHTTP_NO_REQUEST_DATA, 0, 0, 0) &&
					  WinHttpReceiveResponse(request, nullptr) &&
					  WinHttpQueryHeaders(request, WINHTTP_QUERY_STATUS_CODE | WINHTTP_QUERY_FLAG_NUMBER, WINHTTP_HEADER_NAME_BY_INDEX,
						  &status, &statusSize, WINHTTP_NO_HEADER_INDEX) &&
					  status == 206;
			out->clear();
			if (ok)
			{
				out->reserve(static_cast<qsizetype>(to - from + 1));
				char block[65536];
				for (;;)
				{
					DWORD got = 0;
					if (m_cancel->load() || !WinHttpReadData(request, block, sizeof(block), &got))
					{
						ok = false;
						break;
					}
					if (got == 0)
						break;
					out->append(block, static_cast<qsizetype>(got));
				}
				ok = ok && static_cast<u64>(out->size()) == to - from + 1;
			}
			if (ok)
				followRedirect(request);
			WinHttpCloseHandle(request);
			return ok;
		}

		std::atomic<bool>* m_cancel;
		HINTERNET m_session = nullptr;
		HINTERNET m_connect = nullptr;
		std::wstring m_host;
		std::wstring m_path;
	};
#else
	/// The same on libcurl: one handle kept open, so the connection and the storage node it landed on are reused.
	class Net
	{
	public:
		explicit Net(std::atomic<bool>* cancel)
			: m_cancel(cancel)
			, m_curl(curl_easy_init())
			, m_url(BACKUP_URL)
		{
			if (!m_curl)
				return;
			curl_easy_setopt(m_curl, CURLOPT_USERAGENT, "RIPART/1.0");
			curl_easy_setopt(m_curl, CURLOPT_FOLLOWLOCATION, 1L);
			curl_easy_setopt(m_curl, CURLOPT_MAXREDIRS, 5L);
			curl_easy_setopt(m_curl, CURLOPT_REDIR_PROTOCOLS, static_cast<long>(CURLPROTO_HTTPS));
			curl_easy_setopt(m_curl, CURLOPT_CONNECTTIMEOUT, 15L);
			curl_easy_setopt(m_curl, CURLOPT_LOW_SPEED_LIMIT, 1L);
			curl_easy_setopt(m_curl, CURLOPT_LOW_SPEED_TIME, 20L);
			curl_easy_setopt(m_curl, CURLOPT_NOSIGNAL, 1L);
			curl_easy_setopt(m_curl, CURLOPT_WRITEFUNCTION, &Net::receive);
		}

		~Net()
		{
			if (m_curl)
				curl_easy_cleanup(m_curl);
		}

		Net(const Net&) = delete;
		Net& operator=(const Net&) = delete;

		/// The bytes from `from` to `to`, inclusive. Tries again on a server's error: archive.org's nodes answer 500 now and then.
		bool range(u64 from, u64 to, QByteArray* out)
		{
			for (int attempt = 0; attempt < 6; attempt++)
			{
				if (m_cancel->load())
					return false;
				if (rangeOnce(from, to, out))
					return true;
				m_url = BACKUP_URL; // the storage node may be what failed: ask for a new one
				for (int waited = 0; waited < 1000 + attempt * 1500 && !m_cancel->load(); waited += 100)
					std::this_thread::sleep_for(std::chrono::milliseconds(100));
			}
			return false;
		}

	private:
		struct Sink
		{
			QByteArray* out;
			std::atomic<bool>* cancel;
		};

		static size_t receive(char* data, size_t size, size_t count, void* user)
		{
			Sink* sink = static_cast<Sink*>(user);
			if (sink->cancel->load())
				return 0; // ends the transfer
			sink->out->append(data, static_cast<qsizetype>(size * count));
			return size * count;
		}

		bool rangeOnce(u64 from, u64 to, QByteArray* out)
		{
			if (!m_curl)
				return false;
			out->clear();
			out->reserve(static_cast<qsizetype>(to - from + 1));
			Sink sink{out, m_cancel};
			const std::string bytes = std::to_string(from) + "-" + std::to_string(to);
			curl_easy_setopt(m_curl, CURLOPT_URL, m_url.c_str());
			curl_easy_setopt(m_curl, CURLOPT_RANGE, bytes.c_str());
			curl_easy_setopt(m_curl, CURLOPT_WRITEDATA, &sink);
			long status = 0;
			const bool ok = curl_easy_perform(m_curl) == CURLE_OK &&
							curl_easy_getinfo(m_curl, CURLINFO_RESPONSE_CODE, &status) == CURLE_OK && status == 206 &&
							static_cast<u64>(out->size()) == to - from + 1;
			if (ok)
			{
				// where the redirect landed, so the next range goes straight there. Only ever one of archive.org's own hosts
				char* landed = nullptr;
				if (curl_easy_getinfo(m_curl, CURLINFO_EFFECTIVE_URL, &landed) == CURLE_OK && landed != nullptr)
				{
					const std::string url(landed);
					const std::string scheme("https://");
					const size_t hostEnd = url.find('/', scheme.size());
					if (url.rfind(scheme, 0) == 0 && hostEnd != std::string::npos && hostEnd > scheme.size() + 12 &&
						url.compare(hostEnd - 12, 12, ".archive.org") == 0)
						m_url = url;
				}
			}
			return ok;
		}

		std::atomic<bool>* m_cancel;
		CURL* m_curl;
		std::string m_url;
	};
#endif

	struct Piece
	{
		QString file; // SLUS_123.45_COV.png
		QString kind; // COV COV2 ICO LAB LGO BG SCR
		QString member; // its path in the zip
		u64 offset = 0;
		u32 size = 0;
	};

	struct Game
	{
		bool ps2 = true;
		QString id;
		QString title;
		QVector<Piece> pieces;

		bool isFullSet() const
		{
			QSet<QString> have;
			for (const Piece& p : pieces)
				have.insert(p.kind);
			for (const char* kind : {"COV", "COV2", "ICO", "LAB", "LGO", "BG", "SCR"})
				if (!have.contains(QString::fromLatin1(kind)))
					return false;
			return true;
		}
	};

	QString cachePath(const QString& name)
	{
		return QString::fromStdString(Path::Combine(EmuFolders::DataRoot, CACHE_DIR)) + QLatin1Char('/') + name;
	}

	QByteArray readFile(const QString& path)
	{
		QFile f(path);
		return f.open(QIODevice::ReadOnly) ? f.readAll() : QByteArray();
	}

	bool writeFile(const QString& path, const QByteArray& data)
	{
		QDir().mkpath(QFileInfo(path).absolutePath());
		QFile f(path);
		return f.open(QIODevice::WriteOnly) && f.write(data) == data.size();
	}

	u16 le16(const char* p)
	{
		const uchar* b = reinterpret_cast<const uchar*>(p);
		return static_cast<u16>(b[0] | (b[1] << 8));
	}

	u32 le32(const char* p)
	{
		const uchar* b = reinterpret_cast<const uchar*>(p);
		return static_cast<u32>(b[0]) | (static_cast<u32>(b[1]) << 8) | (static_cast<u32>(b[2]) << 16) | (static_cast<u32>(b[3]) << 24);
	}

	u64 le64(const char* p)
	{
		return static_cast<u64>(le32(p)) | (static_cast<u64>(le32(p + 4)) << 32);
	}

	struct DirEntry
	{
		QString name;
		u64 offset;
		u32 size;
	};

	std::vector<DirEntry> parseDirectory(const QByteArray& dir)
	{
		std::vector<DirEntry> rows;
		const char* d = dir.constData();
		const qsizetype total = dir.size();
		qsizetype p = 0;
		while (p + 46 <= total && le32(d + p) == 0x02014b50)
		{
			u64 size = le32(d + p + 24);
			u64 offset = le32(d + p + 42);
			const int nameLen = le16(d + p + 28), extraLen = le16(d + p + 30), commentLen = le16(d + p + 32);
			if (p + 46 + nameLen + extraLen + commentLen > total)
				break;
			// a file past 4 GB has its real offset (and size, if that overflowed too) in the zip64 extra field
			for (qsizetype e = p + 46 + nameLen; e + 4 <= p + 46 + nameLen + extraLen;)
			{
				const int id = le16(d + e), len = le16(d + e + 2);
				if (id == 1)
				{
					qsizetype v = e + 4;
					if (le32(d + p + 24) == 0xffffffffu)
					{
						size = le64(d + v);
						v += 8;
					}
					if (le32(d + p + 20) == 0xffffffffu)
						v += 8;
					if (le32(d + p + 42) == 0xffffffffu)
						offset = le64(d + v);
				}
				e += 4 + len;
			}
			rows.push_back({QString::fromUtf8(d + p + 46, nameLen), offset, static_cast<u32>(size)});
			p += 46 + nameLen + extraLen + commentLen;
		}
		return rows;
	}

	/// ID2 and title from a line of PS2_LIST.csv: ID,ID2,"Title"
	QHash<QString, QString> parseTitles(const QByteArray& csv)
	{
		QHash<QString, QString> titles;
		const QList<QByteArray> lines = csv.split('\n');
		for (const QByteArray& raw : lines)
		{
			const qsizetype a = raw.indexOf(',');
			const qsizetype b = a < 0 ? -1 : raw.indexOf(',', a + 1);
			if (b < 0)
				continue;
			QString title = QString::fromUtf8(raw.mid(b + 1)).trimmed();
			if (title.size() >= 2 && title.startsWith(QLatin1Char('"')) && title.endsWith(QLatin1Char('"')))
				title = title.mid(1, title.size() - 2).replace(QStringLiteral("\"\""), QStringLiteral("\""));
			titles.insert(QString::fromUtf8(raw.mid(a + 1, b - a - 1)), title);
		}
		return titles;
	}

	/// Whichever pieces the local records hold are read from the range, so a local extra field of any size is fine up to 512 bytes.
	bool fetchPiece(Net& net, const Piece& piece, QByteArray* png)
	{
		QByteArray raw;
		const u64 want = 30 + static_cast<u64>(piece.member.toUtf8().size()) + 512 + piece.size;
		if (!net.range(piece.offset, piece.offset + want - 1, &raw) || raw.size() < 30 || le32(raw.constData()) != 0x04034b50)
			return false;
		const qsizetype start = 30 + le16(raw.constData() + 26) + le16(raw.constData() + 28);
		if (start + piece.size > raw.size())
			return false;
		*png = raw.mid(start, piece.size);
		return png->startsWith(QByteArray::fromHex("89504e470d0a1a0a"));
	}

	QByteArray tarHeader(const QByteArray& name, u32 size)
	{
		QByteArray h(512, '\0');
		std::memcpy(h.data(), name.constData(), std::min<size_t>(name.size(), 100));
		std::memcpy(h.data() + 100, "0000644", 7);
		std::memcpy(h.data() + 108, "0000000", 7);
		std::memcpy(h.data() + 116, "0000000", 7);
		const QByteArray octal = QByteArray::number(size, 8).rightJustified(11, '0');
		std::memcpy(h.data() + 124, octal.constData(), 11);
		std::memcpy(h.data() + 136, "00000000000", 11);
		std::memset(h.data() + 148, ' ', 8);
		h[156] = '0';
		std::memcpy(h.data() + 257, "ustar", 6);
		std::memcpy(h.data() + 263, "00", 2);
		unsigned int sum = 0;
		for (int i = 0; i < 512; i++)
			sum += static_cast<uchar>(h[i]);
		const QByteArray check = QByteArray::number(sum, 8).rightJustified(6, '0');
		std::memcpy(h.data() + 148, check.constData(), 6);
		h[154] = '\0';
		h[155] = ' ';
		return h;
	}

	/// The names in a tar, and where its end is: what is already there is kept and added to.
	QSet<QString> tarNames(const QString& path, qint64* end)
	{
		QSet<QString> names;
		*end = 0;
		QFile f(path);
		if (!f.open(QIODevice::ReadOnly))
			return names;
		for (;;)
		{
			f.seek(*end);
			const QByteArray h = f.read(512);
			if (h.size() < 512 || h[0] == '\0')
				break;
			names.insert(QString::fromLatin1(h.constData(), static_cast<int>(qstrnlen(h.constData(), 100))));
			const u64 size = QByteArray(h.constData() + 124, 11).toULongLong(nullptr, 8);
			*end += 512 + static_cast<qint64>((size + 511) / 512 * 512);
		}
		return names;
	}

	QString gameIdOf(const QString& fileName)
	{
		static const QRegularExpression id(QStringLiteral("^([A-Za-z]{4}_\\d{3}\\.\\d{2})"));
		const QRegularExpressionMatch m = id.match(fileName);
		return m.hasMatch() ? m.captured(1).toUpper() : QString();
	}

	QString decoyName(const Game& game)
	{
		QString title;
		for (const QChar c : game.title)
			if (c.unicode() < 127 && (c.isLetterOrNumber() || QStringLiteral(" !&'()+,-").contains(c)))
				title += c;
		title = title.trimmed().left(32).trimmed();
		return game.id + QLatin1Char('.') + (title.isEmpty() ? game.id : title) + QStringLiteral(".iso");
	}

	class Dialog final : public QDialog
	{
	public:
		explicit Dialog(QWidget* parent)
			: QDialog(parent)
		{
			setWindowTitle(QStringLiteral("RIPART"));
			resize(980, 680);
			buildUi();
			startJob(QStringLiteral("Reading the database's list"), [this]() { loadDatabase(); });
			m_thumbThread = std::thread([this]() { thumbLoop(); });
		}

		~Dialog() override
		{
			m_cancel.store(true);
			m_thumbCancel.store(true);
			{
				std::lock_guard<std::mutex> lock(m_thumbMutex);
				m_thumbStop = true;
			}
			m_thumbWake.notify_all();
			if (m_job.joinable())
				m_job.join();
			if (m_thumbThread.joinable())
				m_thumbThread.join();
		}

	private:
		void buildUi()
		{
			QVBoxLayout* top = new QVBoxLayout(this);

			QHBoxLayout* place = new QHBoxLayout();
			place->addWidget(new QLabel(QStringLiteral("Drive or folder:"), this));
			m_root = new QLineEdit(this);
			m_root->setPlaceholderText(QStringLiteral("The top of the drive OPL or RIPPS2 reads, where DVD and ART go"));
			place->addWidget(m_root, 1);
			QPushButton* browse = new QPushButton(QStringLiteral("Browse..."), this);
			place->addWidget(browse);
			m_output = new QComboBox(this);
			m_output->addItem(QStringLiteral("ART folder (OPL and RIPPS2)"));
			m_output->addItem(QStringLiteral("ART/art.tar (RIPPS2 ART Pack, one file)"));
			place->addWidget(m_output);
			top->addLayout(place);
			connect(browse, &QPushButton::clicked, this, [this]() {
				const QString dir = QFileDialog::getExistingDirectory(this, QStringLiteral("The drive or folder"), m_root->text());
				if (!dir.isEmpty())
					m_root->setText(QDir::toNativeSeparators(dir));
			});

			QTabWidget* tabs = new QTabWidget(this);
			tabs->addTab(buildDecoyTab(), QStringLiteral("Decoys"));
			tabs->addTab(buildLibraryTab(), QStringLiteral("Library"));
			top->addWidget(tabs, 1);

			m_status = new QLabel(this);
			m_status->setWordWrap(true);
			top->addWidget(m_status);
			QHBoxLayout* bar = new QHBoxLayout();
			m_progress = new QProgressBar(this);
			bar->addWidget(m_progress, 1);
			m_stop = new QPushButton(QStringLiteral("Stop"), this);
			m_stop->setEnabled(false);
			bar->addWidget(m_stop);
			top->addLayout(bar);
			connect(m_stop, &QPushButton::clicked, this, [this]() { m_cancel.store(true); });

			QLabel* credit = new QLabel(QStringLiteral("Art: OPL Manager's community database, from danielb7390's September 2024 backup on archive.org. "
													   "A decoy is a 2 KB entry for art only and does not start."),
				this);
			credit->setWordWrap(true);
			top->addWidget(credit);
		}

		QWidget* buildDecoyTab()
		{
			QWidget* page = new QWidget(this);
			QVBoxLayout* v = new QVBoxLayout(page);
			QLabel* what = new QLabel(QStringLiteral("Game entries that are only there for their art, so a theme can be judged on a real list with no games on the "
													 "drive. Each one is a full set, picked at random, and it shows in OPL or RIPPS2 straight away. "
													 "Stock OPL needs its art option on."),
				page);
			what->setWordWrap(true);
			v->addWidget(what);
			QHBoxLayout* row = new QHBoxLayout();
			row->addWidget(new QLabel(QStringLiteral("How many:"), page));
			m_decoyCount = new QSpinBox(page);
			m_decoyCount->setRange(1, 500);
			m_decoyCount->setValue(12);
			row->addWidget(m_decoyCount);
			m_decoyGo = new QPushButton(QStringLiteral("Fetch Decoys"), page);
			row->addWidget(m_decoyGo);
			QPushButton* remove = new QPushButton(QStringLiteral("Remove Decoys..."), page);
			row->addWidget(remove);
			row->addStretch(1);
			v->addLayout(row);
			v->addStretch(1);
			connect(m_decoyGo, &QPushButton::clicked, this, [this]() { fetchDecoys(); });
			connect(remove, &QPushButton::clicked, this, [this]() { removeDecoys(); });
			return page;
		}

		QWidget* buildLibraryTab()
		{
			QWidget* page = new QWidget(this);
			QVBoxLayout* v = new QVBoxLayout(page);

			QHBoxLayout* filter = new QHBoxLayout();
			m_search = new QLineEdit(page);
			m_search->setPlaceholderText(QStringLiteral("Search titles and game IDs"));
			filter->addWidget(m_search, 1);
			m_system = new QComboBox(page);
			m_system->addItems({QStringLiteral("PS2"), QStringLiteral("PS1"), QStringLiteral("PS2 and PS1")});
			filter->addWidget(m_system);
			m_onlyTicked = new QCheckBox(QStringLiteral("Only ticked"), page);
			filter->addWidget(m_onlyTicked);
			QPushButton* all = new QPushButton(QStringLiteral("Tick Shown"), page);
			QPushButton* none = new QPushButton(QStringLiteral("Clear All"), page);
			QPushButton* scan = new QPushButton(QStringLiteral("Find Games With No Art"), page);
			filter->addWidget(all);
			filter->addWidget(none);
			filter->addWidget(scan);
			v->addLayout(filter);

			QSplitter* split = new QSplitter(page);
			m_list = new QTreeWidget(split);
			m_list->setColumnCount(3);
			m_list->setHeaderLabels({QStringLiteral("Game ID"), QStringLiteral("Title"), QStringLiteral("Art")});
			m_list->setRootIsDecorated(false);
			m_list->setUniformRowHeights(true);
			m_list->header()->setStretchLastSection(false);
			m_list->header()->setSectionResizeMode(1, QHeaderView::Stretch);

			QWidget* right = new QWidget(split);
			QVBoxLayout* rv = new QVBoxLayout(right);
			rv->setContentsMargins(0, 0, 0, 0);
			rv->addWidget(new QLabel(QStringLiteral("Art to fetch, every game:"), right));
			QGridLayout* kinds = new QGridLayout();
			int n = 0;
			for (const char* kind : {"COV", "COV2", "ICO", "LAB", "LGO", "BG", "SCR"})
			{
				QCheckBox* box = new QCheckBox(QString::fromLatin1(kind), right);
				box->setChecked(true);
				m_kinds.insert(QString::fromLatin1(kind), box);
				kinds->addWidget(box, n / 4, n % 4);
				n++;
			}
			rv->addLayout(kinds);
			m_pieceTitle = new QLabel(QStringLiteral("Pick a game to choose between its art."), right);
			m_pieceTitle->setWordWrap(true);
			rv->addWidget(m_pieceTitle);
			m_pieces = new QListWidget(right);
			m_pieces->setViewMode(QListView::IconMode);
			m_pieces->setResizeMode(QListView::Adjust);
			m_pieces->setIconSize(QSize(128, 96));
			m_pieces->setGridSize(QSize(146, 128));
			m_pieces->setWordWrap(true);
			m_pieces->setMovement(QListView::Static);
			rv->addWidget(m_pieces, 1);
			split->setStretchFactor(0, 3);
			split->setStretchFactor(1, 2);
			v->addWidget(split, 1);

			QHBoxLayout* go = new QHBoxLayout();
			m_withDecoys = new QCheckBox(QStringLiteral("Add a decoy entry for each"), page);
			go->addWidget(m_withDecoys);
			go->addStretch(1);
			m_tickedLabel = new QLabel(page);
			go->addWidget(m_tickedLabel);
			m_fetchGo = new QPushButton(QStringLiteral("Fetch Ticked"), page);
			go->addWidget(m_fetchGo);
			v->addLayout(go);

			m_searchTimer = new QTimer(this);
			m_searchTimer->setSingleShot(true);
			m_searchTimer->setInterval(180);
			connect(m_searchTimer, &QTimer::timeout, this, [this]() { applyFilter(); });
			connect(m_search, &QLineEdit::textChanged, this, [this]() { m_searchTimer->start(); });
			connect(m_system, &QComboBox::currentIndexChanged, this, [this]() { applyFilter(); });
			connect(m_onlyTicked, &QCheckBox::toggled, this, [this]() { applyFilter(); });
			connect(all, &QPushButton::clicked, this, [this]() { tickShown(true); });
			connect(none, &QPushButton::clicked, this, [this]() {
				m_filling = true;
				for (int i = 0; i < m_list->topLevelItemCount(); i++)
					m_list->topLevelItem(i)->setCheckState(0, Qt::Unchecked);
				m_filling = false;
				countTicked();
			});
			connect(scan, &QPushButton::clicked, this, [this]() { scanDrive(); });
			connect(m_list, &QTreeWidget::itemChanged, this, [this]() {
				if (!m_filling)
					countTicked();
			});
			connect(m_list, &QTreeWidget::currentItemChanged, this, [this](QTreeWidgetItem* item) { showPieces(item); });
			connect(m_pieces, &QListWidget::itemChanged, this, [this](QListWidgetItem* item) {
				if (m_fillingPieces)
					return;
				const QString file = item->data(Qt::UserRole).toString();
				if (item->checkState() == Qt::Checked)
					m_refused.remove(file);
				else
					m_refused.insert(file);
			});
			connect(m_fetchGo, &QPushButton::clicked, this, [this]() { fetchTicked(); });
			return page;
		}

		// ---- jobs: one at a time, off the UI thread ----

		template <typename F>
		void ui(F&& f)
		{
			QMetaObject::invokeMethod(this, std::forward<F>(f), Qt::QueuedConnection);
		}

		void say(const QString& text)
		{
			ui([this, text]() { m_status->setText(text); });
		}

		void progress(int done, int total)
		{
			ui([this, done, total]() {
				m_progress->setRange(0, total);
				m_progress->setValue(done);
			});
		}

		void setBusy(bool busy)
		{
			m_decoyGo->setEnabled(!busy && !m_games.empty());
			m_fetchGo->setEnabled(!busy && !m_games.empty());
			m_stop->setEnabled(busy);
		}

		void startJob(const QString& text, std::function<void()> work)
		{
			if (m_job.joinable())
				m_job.join();
			m_cancel.store(false);
			m_status->setText(text);
			setBusy(true);
			m_job = std::thread([this, work = std::move(work)]() {
				work();
				ui([this]() { setBusy(false); });
			});
		}

		// ---- the database ----

		void loadDatabase()
		{
			Net net(&m_cancel);
			QHash<QString, QString> titles[2];
			const QString name = QString::fromLatin1(CACHE_NAME);
			const QString dirPath = cachePath(name + QStringLiteral(".dir"));
			QByteArray dir = readFile(dirPath);
			if (static_cast<u64>(dir.size()) != BACKUP_DIR_SIZE)
			{
				say(QStringLiteral("Reading the database's list from archive.org (8.6 MB, once)"));
				if (!net.range(BACKUP_DIR_OFFSET, BACKUP_DIR_OFFSET + BACKUP_DIR_SIZE - 1, &dir) || !writeFile(dirPath, dir))
				{
					say(QStringLiteral("archive.org did not answer. Close this and try again."));
					return;
				}
			}
			const std::vector<DirEntry> rows = parseDirectory(dir);

			int which = 0;
			for (const char* list : {"PS2_LIST.csv", "PS1_LIST.csv"})
			{
				const QString file = QString::fromLatin1(list);
				const QString path = cachePath(name + QLatin1Char('_') + file);
				QByteArray text = readFile(path);
				if (text.isEmpty())
				{
					for (const DirEntry& row : rows)
					{
						if (row.name != file)
							continue;
						QByteArray raw;
						const u64 want = 30 + static_cast<u64>(row.name.size()) + 512 + row.size;
						if (net.range(row.offset, row.offset + want - 1, &raw) && raw.size() > 30)
						{
							text = raw.mid(30 + le16(raw.constData() + 26) + le16(raw.constData() + 28), row.size);
							writeFile(path, text);
						}
						break;
					}
				}
				titles[which++] = parseTitles(text);
			}

			auto games = std::make_shared<std::vector<Game>>();
			QHash<QString, int> index;
			for (const DirEntry& row : rows)
			{
				const QStringList parts = row.name.split(QLatin1Char('/'));
				if (parts.size() != 3 || !parts[2].endsWith(QStringLiteral(".png"), Qt::CaseInsensitive))
					continue;
				const QString key = parts[0] + QLatin1Char('/') + parts[1];
				auto found = index.constFind(key);
				int at;
				if (found == index.constEnd())
				{
					at = static_cast<int>(games->size());
					index.insert(key, at);
					Game g;
					g.ps2 = parts[0] == QStringLiteral("PS2");
					g.id = parts[1];
					g.title = titles[g.ps2 ? 0 : 1].value(parts[1]);
					games->push_back(std::move(g));
				}
				else
					at = found.value();
				Piece p;
				p.file = parts[2];
				p.member = row.name;
				p.offset = row.offset;
				p.size = row.size;
				QString stem = parts[2].mid(parts[1].size() + 1);
				stem.chop(4);
				p.kind = stem.section(QLatin1Char('_'), 0, 0);
				(*games)[at].pieces.push_back(std::move(p));
			}
			if (games->empty())
			{
				say(QStringLiteral("The database's list could not be read."));
				return;
			}
			ui([this, games]() {
				m_games = std::move(*games);
				fillList();
			});
		}

		void fillList()
		{
			m_filling = true;
			m_list->setSortingEnabled(false);
			m_list->clear();
			QList<QTreeWidgetItem*> items;
			items.reserve(static_cast<int>(m_games.size()));
			for (size_t i = 0; i < m_games.size(); i++)
			{
				const Game& g = m_games[i];
				QTreeWidgetItem* item = new QTreeWidgetItem(QStringList{g.id, g.title, QString::number(g.pieces.size())});
				item->setCheckState(0, Qt::Unchecked);
				item->setData(0, Qt::UserRole, static_cast<qulonglong>(i));
				items.append(item);
			}
			m_list->addTopLevelItems(items);
			m_list->resizeColumnToContents(0);
			m_list->setSortingEnabled(true);
			m_list->sortByColumn(1, Qt::AscendingOrder);
			m_filling = false;
			applyFilter();
			setBusy(false);
			int full = 0;
			for (const Game& g : m_games)
				full += g.ps2 && g.isFullSet();
			m_status->setText(QStringLiteral("%1 games in the database, %2 of them PS2 full sets.").arg(m_games.size()).arg(full));
		}

		const Game& gameOf(const QTreeWidgetItem* item) const
		{
			return m_games[item->data(0, Qt::UserRole).toULongLong()];
		}

		void applyFilter()
		{
			const QString text = m_search->text().trimmed();
			const int system = m_system->currentIndex();
			const bool ticked = m_onlyTicked->isChecked();
			m_list->setUpdatesEnabled(false);
			for (int i = 0; i < m_list->topLevelItemCount(); i++)
			{
				QTreeWidgetItem* item = m_list->topLevelItem(i);
				const Game& g = gameOf(item);
				const bool show = (system == 2 || g.ps2 == (system == 0)) && (!ticked || item->checkState(0) == Qt::Checked) &&
								  (text.isEmpty() || g.title.contains(text, Qt::CaseInsensitive) || g.id.contains(text, Qt::CaseInsensitive));
				item->setHidden(!show);
			}
			m_list->setUpdatesEnabled(true);
			countTicked();
		}

		void tickShown(bool on)
		{
			m_filling = true;
			for (int i = 0; i < m_list->topLevelItemCount(); i++)
				if (!m_list->topLevelItem(i)->isHidden())
					m_list->topLevelItem(i)->setCheckState(0, on ? Qt::Checked : Qt::Unchecked);
			m_filling = false;
			countTicked();
		}

		void countTicked()
		{
			int n = 0;
			for (int i = 0; i < m_list->topLevelItemCount(); i++)
				n += m_list->topLevelItem(i)->checkState(0) == Qt::Checked;
			m_tickedLabel->setText(QStringLiteral("%1 ticked").arg(n));
		}

		// ---- what is on the drive ----

		QString rootPath() const
		{
			return QDir::fromNativeSeparators(m_root->text().trimmed());
		}

		bool haveRoot()
		{
			const QString root = rootPath();
			if (!root.isEmpty() && QDir(root).exists())
				return true;
			QMessageBox::information(this, QStringLiteral("RIPART"), QStringLiteral("Pick a drive or folder first."));
			return false;
		}

		QSet<QString> artOnDrive(const QString& root) const
		{
			QSet<QString> names;
			QDir art(root + QStringLiteral("/ART"));
			const QStringList files = art.entryList(QDir::Files);
			for (const QString& f : files)
				names.insert(f.toUpper());
			qint64 end = 0;
			const QSet<QString> packed = tarNames(art.filePath(QStringLiteral("art.tar")), &end);
			for (const QString& f : packed)
				names.insert(f.toUpper());
			return names;
		}

		void scanDrive()
		{
			if (!haveRoot() || m_games.empty())
				return;
			const QString root = rootPath();
			const QSet<QString> art = artOnDrive(root);
			QSet<QString> ids;
			int unnamed = 0;
			for (const char* folder : {"DVD", "CD", "POPS"})
			{
				const QStringList files = QDir(root + QLatin1Char('/') + QString::fromLatin1(folder)).entryList({QStringLiteral("*.iso"), QStringLiteral("*.zso"), QStringLiteral("*.vcd")}, QDir::Files);
				for (const QString& f : files)
				{
					const QString id = gameIdOf(f);
					if (id.isEmpty())
						unnamed++;
					else
						ids.insert(id);
				}
			}
			QSet<QString> bare;
			for (const QString& id : ids)
			{
				const QString cov = id.toUpper() + QStringLiteral("_COV.PNG");
				if (!art.contains(cov))
					bare.insert(id);
			}
			int found = 0;
			m_filling = true;
			for (int i = 0; i < m_list->topLevelItemCount(); i++)
			{
				QTreeWidgetItem* item = m_list->topLevelItem(i);
				const bool want = bare.contains(gameOf(item).id);
				item->setCheckState(0, want ? Qt::Checked : Qt::Unchecked);
				found += want;
			}
			m_filling = false;
			m_system->setCurrentIndex(2);
			m_onlyTicked->setChecked(true);
			applyFilter();
			m_status->setText(QStringLiteral("%1 games on this drive, %2 with no cover, %3 of those in the database and ticked. %4 files with no game ID in their name.")
								  .arg(ids.size())
								  .arg(bare.size())
								  .arg(found)
								  .arg(unnamed));
		}

		void removeDecoys()
		{
			if (!haveRoot())
				return;
			QDir dvd(rootPath() + QStringLiteral("/DVD"));
			QStringList decoys;
			const QStringList files = dvd.entryList({QStringLiteral("*.iso")}, QDir::Files);
			for (const QString& f : files)
			{
				if (QFileInfo(dvd.filePath(f)).size() != DECOY_BYTES || gameIdOf(f).isEmpty())
					continue;
				const QByteArray bytes = readFile(dvd.filePath(f));
				if (bytes == QByteArray(DECOY_BYTES, '\0'))
					decoys.append(f);
			}
			if (decoys.isEmpty())
			{
				m_status->setText(QStringLiteral("No decoys in that DVD folder."));
				return;
			}
			if (QMessageBox::question(this, QStringLiteral("RIPART"), QStringLiteral("Remove %1 decoy entries from the DVD folder? Their art stays in ART.").arg(decoys.size())) != QMessageBox::Yes)
				return;
			for (const QString& f : decoys)
				dvd.remove(f);
			m_status->setText(QStringLiteral("%1 decoys removed.").arg(decoys.size()));
		}

		// ---- fetching ----

		std::vector<Piece> piecesFor(const Game& g) const
		{
			std::vector<Piece> out;
			for (const Piece& p : g.pieces)
			{
				const QCheckBox* box = m_kinds.value(p.kind, nullptr);
				if ((box == nullptr || box->isChecked()) && !m_refused.contains(p.file))
					out.push_back(p);
			}
			return out;
		}

		void fetchDecoys()
		{
			if (m_games.empty() || !haveRoot())
				return;
			const QString root = rootPath();
			QDir dvd(root + QStringLiteral("/DVD"));
			QSet<QString> there;
			const QStringList files = dvd.entryList(QDir::Files);
			for (const QString& f : files)
				there.insert(gameIdOf(f));
			std::vector<int> pool;
			for (size_t i = 0; i < m_games.size(); i++)
				if (m_games[i].ps2 && !m_games[i].title.isEmpty() && m_games[i].isFullSet() && !there.contains(m_games[i].id))
					pool.push_back(static_cast<int>(i));
			const int count = std::min<int>(m_decoyCount->value(), static_cast<int>(pool.size()));
			std::vector<Piece> pieces;
			QStringList names;
			for (int i = 0; i < count; i++)
			{
				const int pick = i + QRandomGenerator::global()->bounded(static_cast<int>(pool.size()) - i);
				std::swap(pool[i], pool[pick]);
				const Game& g = m_games[pool[i]];
				names.append(decoyName(g));
				for (const Piece& p : g.pieces)
					pieces.push_back(p);
			}
			run(root, std::move(pieces), names);
		}

		void fetchTicked()
		{
			if (m_games.empty() || !haveRoot())
				return;
			std::vector<Piece> pieces;
			QStringList names;
			for (int i = 0; i < m_list->topLevelItemCount(); i++)
			{
				const QTreeWidgetItem* item = m_list->topLevelItem(i);
				if (item->checkState(0) != Qt::Checked)
					continue;
				const Game& g = gameOf(item);
				const std::vector<Piece> mine = piecesFor(g);
				pieces.insert(pieces.end(), mine.begin(), mine.end());
				if (m_withDecoys->isChecked() && g.ps2)
					names.append(decoyName(g));
			}
			if (pieces.empty())
			{
				m_status->setText(QStringLiteral("Nothing ticked."));
				return;
			}
			run(rootPath(), std::move(pieces), names);
		}

		void run(const QString& root, std::vector<Piece> pieces, const QStringList& decoys)
		{
			const bool tar = m_output->currentIndex() == 1;
			startJob(QStringLiteral("Fetching"), [this, root, pieces = std::move(pieces), decoys, tar]() { fetch(root, pieces, decoys, tar); });
		}

		void fetch(const QString& root, const std::vector<Piece>& pieces, const QStringList& decoys, bool tar)
		{
			const QString artDir = root + QStringLiteral("/ART");
			QDir().mkpath(artDir);

			if (!decoys.isEmpty())
			{
				QDir().mkpath(root + QStringLiteral("/DVD"));
				for (const QString& name : decoys)
				{
					const QString path = root + QStringLiteral("/DVD/") + name;
					if (!QFileInfo::exists(path)) // never over a real game
						writeFile(path, QByteArray(DECOY_BYTES, '\0'));
				}
			}

			QFile pack(artDir + QStringLiteral("/art.tar"));
			QSet<QString> have;
			qint64 end = 0;
			if (tar)
			{
				have = tarNames(pack.fileName(), &end);
				if (!pack.open(QIODevice::ReadWrite))
				{
					say(QStringLiteral("Could not write %1.").arg(pack.fileName()));
					return;
				}
				pack.resize(end);
				pack.seek(end);
			}

			Net net(&m_cancel);
			int done = 0, wrote = 0, kept = 0, failed = 0;
			const int total = static_cast<int>(pieces.size());
			progress(0, total);
			for (const Piece& p : pieces)
			{
				if (m_cancel.load())
					break;
				const bool there = tar ? have.contains(p.file) : QFileInfo::exists(artDir + QLatin1Char('/') + p.file);
				if (there)
					kept++;
				else
				{
					QByteArray png = cachedThumb(p.file);
					if (png.isEmpty() && !fetchPiece(net, p, &png))
					{
						if (!m_cancel.load())
							failed++;
					}
					else if (tar)
					{
						pack.write(tarHeader(p.file.toLatin1(), static_cast<u32>(png.size())));
						pack.write(png);
						pack.write(QByteArray((512 - png.size() % 512) % 512, '\0'));
						wrote++;
					}
					else if (writeFile(artDir + QLatin1Char('/') + p.file, png))
						wrote++;
					else
						failed++;
				}
				progress(++done, total);
				say(QStringLiteral("%1 of %2: %3").arg(done).arg(total).arg(p.file));
			}
			if (tar)
			{
				pack.write(QByteArray(1024, '\0'));
				pack.close();
			}
			const QString decoyNote = decoys.isEmpty() ? QString() : QStringLiteral("%1 decoys, ").arg(decoys.size());
			say(QStringLiteral("%1%2 pieces written, %3 already there, %4 failed%5")
					.arg(decoyNote)
					.arg(wrote)
					.arg(kept)
					.arg(failed)
					.arg(m_cancel.load() ? QStringLiteral(", stopped.") : QStringLiteral(".")));
		}

		// ---- one game's pieces, to choose between ----

		QByteArray cachedThumb(const QString& file)
		{
			std::lock_guard<std::mutex> lock(m_thumbMutex);
			return m_thumbs.value(file);
		}

		void showPieces(QTreeWidgetItem* item)
		{
			m_fillingPieces = true;
			m_pieces->clear();
			m_fillingPieces = false;
			if (item == nullptr)
				return;
			const Game& g = gameOf(item);
			m_pieceTitle->setText(QStringLiteral("%1: untick a piece to leave it out. The full set is ticked to start.").arg(g.title.isEmpty() ? g.id : g.title));
			m_fillingPieces = true;
			std::vector<Piece> wanted;
			for (const Piece& p : g.pieces)
			{
				QListWidgetItem* row = new QListWidgetItem(p.file.mid(g.id.size() + 1).section(QLatin1Char('.'), 0, 0), m_pieces);
				row->setFlags(row->flags() | Qt::ItemIsUserCheckable);
				row->setCheckState(m_refused.contains(p.file) ? Qt::Unchecked : Qt::Checked);
				row->setData(Qt::UserRole, p.file);
				const QByteArray png = cachedThumb(p.file);
				if (png.isEmpty())
					wanted.push_back(p);
				else
					setThumb(row, png);
			}
			m_fillingPieces = false;
			{
				std::lock_guard<std::mutex> lock(m_thumbMutex);
				m_thumbWanted = std::move(wanted);
				m_thumbGen++;
			}
			m_thumbWake.notify_all();
		}

		void setThumb(QListWidgetItem* row, const QByteArray& png)
		{
			QPixmap pixmap;
			if (pixmap.loadFromData(png))
			{
				m_fillingPieces = true;
				row->setIcon(QIcon(pixmap.scaled(m_pieces->iconSize(), Qt::KeepAspectRatio, Qt::SmoothTransformation)));
				m_fillingPieces = false;
			}
		}

		void thumbLoop()
		{
			Net net(&m_thumbCancel);
			for (;;)
			{
				Piece piece;
				unsigned int gen;
				{
					std::unique_lock<std::mutex> lock(m_thumbMutex);
					m_thumbWake.wait(lock, [this]() { return m_thumbStop || !m_thumbWanted.empty(); });
					if (m_thumbStop)
						return;
					piece = m_thumbWanted.front();
					m_thumbWanted.erase(m_thumbWanted.begin());
					gen = m_thumbGen;
				}
				QByteArray png;
				if (!fetchPiece(net, piece, &png))
					continue;
				{
					std::lock_guard<std::mutex> lock(m_thumbMutex);
					m_thumbs.insert(piece.file, png);
				}
				const QString file = piece.file;
				ui([this, file, png, gen]() {
					if (gen != m_thumbGen.load())
						return;
					for (int i = 0; i < m_pieces->count(); i++)
						if (m_pieces->item(i)->data(Qt::UserRole).toString() == file)
							setThumb(m_pieces->item(i), png);
				});
			}
		}

		QLineEdit* m_root = nullptr;
		QComboBox* m_output = nullptr;
		QLabel* m_status = nullptr;
		QProgressBar* m_progress = nullptr;
		QPushButton* m_stop = nullptr;
		QSpinBox* m_decoyCount = nullptr;
		QPushButton* m_decoyGo = nullptr;
		QLineEdit* m_search = nullptr;
		QComboBox* m_system = nullptr;
		QCheckBox* m_onlyTicked = nullptr;
		QTreeWidget* m_list = nullptr;
		QLabel* m_pieceTitle = nullptr;
		QListWidget* m_pieces = nullptr;
		QCheckBox* m_withDecoys = nullptr;
		QLabel* m_tickedLabel = nullptr;
		QPushButton* m_fetchGo = nullptr;
		QTimer* m_searchTimer = nullptr;
		QHash<QString, QCheckBox*> m_kinds;

		std::vector<Game> m_games;
		QSet<QString> m_refused;
		bool m_filling = false;
		bool m_fillingPieces = false;

		std::thread m_job;
		std::atomic<bool> m_cancel{false};

		std::thread m_thumbThread;
		std::mutex m_thumbMutex;
		std::condition_variable m_thumbWake;
		std::vector<Piece> m_thumbWanted;
		QHash<QString, QByteArray> m_thumbs;
		std::atomic<unsigned int> m_thumbGen{0};
		std::atomic<bool> m_thumbCancel{false};
		bool m_thumbStop = false;
	};
} // namespace

void RIPART::Open(QWidget* parent)
{
	Dialog dialog(parent);
	dialog.exec();
}
