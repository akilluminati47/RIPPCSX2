// SPDX-FileCopyrightText: 2002-2026 PCSX2 Dev Team
// SPDX-License-Identifier: GPL-3.0+

#include "RIPPCSX2Menu.h"

#include "MainWindow.h"
#include "QtHost.h"
#include "QtUtils.h"
#include "SettingWidgetBinder.h"

#include "pcsx2/BuildVersion.h"
#include "pcsx2/COP0.h"
#include "pcsx2/Config.h"
#include "pcsx2/GS.h"
#include "pcsx2/GS/GS.h"
#include "pcsx2/Host.h"
#include "pcsx2/MTGS.h"
#include "pcsx2/VMManager.h"

#include "common/Path.h"

#include <QtCore/QDateTime>
#include <QtCore/QDir>
#include <QtCore/QFile>
#include <QtCore/QFileInfo>
#include <QtCore/QPointer>
#include <QtCore/QTextStream>
#include <QtCore/QTimer>
#include <QtCore/QUrl>
#include <QtGui/QClipboard>
#include <QtGui/QFontDatabase>
#include <QtGui/QGuiApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QFileDialog>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QMessageBox>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>

#include <functional>
#include <memory>

#ifdef _WIN32
#include "common/RedtapeWindows.h"
#include <thread>
#endif

namespace
{
	constexpr const char* SITE_URL = "https://akilluminati47.github.io/RIPPCSX2/";
	constexpr const char* REPO_URL = "https://github.com/akilluminati47/RIPPCSX2";
	constexpr const char* LOG_NAME = "emulog.txt";

	// OPL's compatibility modes, with what each one does (RiptOPL's include/iosupport.h and its hints).
	struct OplMode
	{
		const char* name;
		const char* tip;
	};
	constexpr OplMode OPL_MODES[8] = {
		{"Mode 1: Accurate Reads", "Reads at the disc's own timing instead of as fast as the drive can."},
		{"Mode 2: Synchronous Mode", "Reads block until they finish, for games that break on asynchronous ones."},
		{"Mode 3: Unhook Syscalls", "Takes OPL's hooks back out of the kernel once the game has started."},
		{"Mode 4: Skip Videos", "Gives PSS videos a size of zero and skips Bink ones, to get past a video that hangs."},
		{"Mode 5: Emulate DVD-DL", "Answers as a dual layer disc would."},
		{"Mode 6: Disable IGR", "Turns off the in-game reset and in-game menu for games that clash with their hook."},
		{"Mode 7: Buffer overrun fix", "Neutrino only: fixes a game's buffer overrun."},
		{"Mode 8: Slow Reads", "Accurate Reads with DVD media at the CD rate, for games whose audio breaks under Mode 1."},
	};

	QString runningName()
	{
		if (!VMManager::HasValidVM())
			return {};
		std::string serial = VMManager::GetDiscSerial();
		if (!serial.empty())
			return QString::fromStdString(serial);
		std::string elf = VMManager::GetCurrentELF();
		if (!elf.empty())
			return QFileInfo(QString::fromStdString(elf)).completeBaseName();
		return QStringLiteral("BIOS");
	}

	u64 gsReg(u32 offset)
	{
		return *reinterpret_cast<const u64*>(&g_RealGSMem[offset]);
	}

	QString modeName(u64 smode1, u64 smode2)
	{
		const u32 lc = smode1 & 0x7f;
		const u32 cmod = (smode1 >> 13) & 3;
		const bool interlaced = smode2 & 1;
		if (lc == 22)
			return interlaced ? QStringLiteral("1080i") : QStringLiteral("720p");
		if (lc == 32 && cmod == 2)
			return QStringLiteral("NTSC (480i)");
		if (lc == 32 && cmod == 3)
			return QStringLiteral("PAL (576i)");
		if (lc == 32 && cmod == 0)
			return QStringLiteral("480p");
		return QStringLiteral("LC %1 CMOD %2").arg(lc).arg(cmod);
	}

	/// What a test wants to know about the machine right now, as text.
	QString labReport()
	{
		QString s;
		QTextStream out(&s);
		out << "RIPPCSX2 build  " << BuildVersion::GitRev << "\n";
		if (!VMManager::HasValidVM())
		{
			out << "Machine         nothing running\n";
		}
		else
		{
			out << "Title           " << QString::fromStdString(VMManager::GetTitle(true)) << "\n";
			out << "Serial          " << QString::fromStdString(VMManager::GetDiscSerial()) << "\n";
			out << "ELF             " << QString::fromStdString(VMManager::GetCurrentELF()) << "\n";
			out << "CRC             " << QStringLiteral("%1").arg(VMManager::GetCurrentCRC(), 8, 16, QLatin1Char('0')).toUpper() << "\n";
			const u64 pm = gsReg(0x00), sm1 = gsReg(0x10), sm2 = gsReg(0x20), sv = gsReg(0x60);
			out << "\nVideo mode      " << modeName(sm1, sm2) << "\n";
			out << "PMODE           " << Qt::hex << pm << Qt::dec << "   EN1 " << (pm & 1) << " EN2 " << ((pm >> 1) & 1) << "\n";
			out << "SMODE1          " << Qt::hex << sm1 << Qt::dec << "   LC " << (sm1 & 0x7f) << " CMOD " << ((sm1 >> 13) & 3) << "\n";
			out << "SMODE2          " << Qt::hex << sm2 << Qt::dec << "   INT " << (sm2 & 1) << " FFMD " << ((sm2 >> 1) & 1) << "\n";
			out << "SYNCV           " << Qt::hex << sv << Qt::dec << "\n";
			for (int i = 0; i < 2; i++)
			{
				const u64 fb = gsReg(i ? 0x90 : 0x70), d = gsReg(i ? 0xA0 : 0x80);
				out << "DISPFB" << (i + 1) << "         FBP " << (fb & 0x1ff) << " FBW " << ((fb >> 9) & 0x3f) << " PSM " << ((fb >> 15) & 0x1f)
					<< " DBX " << ((fb >> 32) & 0x7ff) << " DBY " << ((fb >> 43) & 0x7ff) << "\n";
				out << "DISPLAY" << (i + 1) << "        DX " << (d & 0xfff) << " DY " << ((d >> 12) & 0x7ff) << " MAGH " << ((d >> 23) & 0xf)
					<< " MAGV " << ((d >> 27) & 3) << " DW " << ((d >> 32) & 0xfff) << " DH " << ((d >> 44) & 0x7ff) << "\n";
			}
		}
		out << "\nEE data write breakpoint\n";
		out << "  Emulated      " << (EmuConfig.DataWriteBreakpoint ? "yes" : "no (as stock PCSX2)") << "\n";
		out << "  Armed         " << (eeDataWriteBpArmed() ? "yes" : "no") << "\n";
		out << "  BPC / DAB / DABM   " << Qt::hex << eeDebugRegs.BPC << " / " << eeDebugRegs.DAB << " / " << eeDebugRegs.DABM << Qt::dec << "\n";
		out << "  Hits          " << eeDataWriteBpHits() << ", last at " << Qt::hex << eeDataWriteBpLastPC() << Qt::dec << "\n";
		out << "\nHDTV output     " << (EmuConfig.GS.HDTVOutput ? "on" : "off") << "\n";
		out << "PINE            " << (EmuConfig.EnablePINE ? QStringLiteral("on, slot %1").arg(EmuConfig.PINESlot) : QStringLiteral("off")) << "\n";
		out << "Host filesystem " << (EmuConfig.HostFs ? "on" : "off") << "\n";
		return s;
	}

	void openFolder(QWidget* parent, const std::string& path)
	{
		QDir().mkpath(QString::fromStdString(path));
		QtUtils::OpenURL(parent, QUrl::fromLocalFile(QString::fromStdString(path)));
	}

	QString logPath()
	{
		return QString::fromStdString(Path::Combine(EmuFolders::Logs, LOG_NAME));
	}

	QString logTail(int lines)
	{
		QFile f(logPath());
		if (!f.open(QIODevice::ReadOnly | QIODevice::Text))
			return {};
		const qint64 keep = 16 * 1024;
		if (f.size() > keep)
			f.seek(f.size() - keep);
		QStringList all = QString::fromUtf8(f.readAll()).split(QLatin1Char('\n'));
		if (all.size() > lines)
			all = all.mid(all.size() - lines);
		return all.join(QLatin1Char('\n'));
	}

	void showMonitor(QWidget* parent)
	{
		static QPointer<QDialog> s_monitor;
		if (s_monitor)
		{
			s_monitor->show();
			s_monitor->raise();
			s_monitor->activateWindow();
			return;
		}
		QDialog* d = new QDialog(parent);
		s_monitor = d;
		d->setAttribute(Qt::WA_DeleteOnClose);
		d->setWindowTitle(QStringLiteral("RIPPCSX2 Lab Monitor"));
		d->resize(620, 520);
		QVBoxLayout* layout = new QVBoxLayout(d);
		QPlainTextEdit* text = new QPlainTextEdit(d);
		text->setReadOnly(true);
		text->setFont(QFontDatabase::systemFont(QFontDatabase::FixedFont));
		layout->addWidget(text);
		QHBoxLayout* row = new QHBoxLayout();
		QPushButton* copy = new QPushButton(QStringLiteral("Copy"), d);
		QPushButton* log = new QPushButton(QStringLiteral("Open Log"), d);
		QPushButton* close = new QPushButton(QStringLiteral("Close"), d);
		row->addWidget(copy);
		row->addWidget(log);
		row->addStretch(1);
		row->addWidget(close);
		layout->addLayout(row);
		QObject::connect(copy, &QPushButton::clicked, d, [text]() { QGuiApplication::clipboard()->setText(text->toPlainText()); });
		QObject::connect(log, &QPushButton::clicked, d, [d]() { QtUtils::OpenURL(d, QUrl::fromLocalFile(logPath())); });
		QObject::connect(close, &QPushButton::clicked, d, &QDialog::close);
		QTimer* timer = new QTimer(d);
		auto refresh = [text]() {
			const QString now = labReport();
			if (now != text->toPlainText())
				text->setPlainText(now);
		};
		QObject::connect(timer, &QTimer::timeout, d, refresh);
		refresh();
		timer->start(500);
		d->show();
	}

	/// The first step towards a list of the whole library: one game, one honest report, on disk where a script can read it.
	void showReport(QWidget* parent)
	{
		QDialog dialog(parent);
		dialog.setWindowTitle(QStringLiteral("RIPPCSX2 Compatibility Report"));
		QVBoxLayout* layout = new QVBoxLayout(&dialog);
		QFormLayout* form = new QFormLayout();
		const QString name = runningName();
		QLabel* what = new QLabel(name.isEmpty() ? QStringLiteral("Nothing is running: the report will only hold your notes.") :
												   QStringLiteral("%1  %2").arg(name, QString::fromStdString(VMManager::GetTitle(true))), &dialog);
		what->setWordWrap(true);
		form->addRow(QStringLiteral("Testing"), what);
		QComboBox* loader = new QComboBox(&dialog);
		loader->addItems({QStringLiteral("OPL / RiptOPL"), QStringLiteral("RIPPS2"), QStringLiteral("Neutrino"), QStringLiteral("Disc image, no loader"), QStringLiteral("ELF on its own"), QStringLiteral("Other")});
		form->addRow(QStringLiteral("Started through"), loader);
		QComboBox* result = new QComboBox(&dialog);
		result->addItems({QStringLiteral("Not tested yet"), QStringLiteral("Black screen"), QStringLiteral("Hangs at boot"), QStringLiteral("Crashes"), QStringLiteral("Boots, menus only"), QStringLiteral("In game, with problems"), QStringLiteral("Playable"), QStringLiteral("Perfect")});
		form->addRow(QStringLiteral("Result"), result);
		layout->addLayout(form);
		QGroupBox* modes = new QGroupBox(QStringLiteral("OPL compatibility modes used"), &dialog);
		QGridLayout* grid = new QGridLayout(modes);
		QCheckBox* boxes[8];
		for (int i = 0; i < 8; i++)
		{
			boxes[i] = new QCheckBox(QString::fromUtf8(OPL_MODES[i].name), modes);
			boxes[i]->setToolTip(QString::fromUtf8(OPL_MODES[i].tip));
			grid->addWidget(boxes[i], i / 2, i % 2);
		}
		layout->addWidget(modes);
		layout->addWidget(new QLabel(QStringLiteral("Notes: what you did, what you saw, what fixed it"), &dialog));
		QPlainTextEdit* notes = new QPlainTextEdit(&dialog);
		notes->setMinimumHeight(90);
		layout->addWidget(notes);
		QCheckBox* shot = new QCheckBox(QStringLiteral("Save a screenshot with the report"), &dialog);
		shot->setChecked(VMManager::HasValidVM());
		shot->setEnabled(VMManager::HasValidVM());
		layout->addWidget(shot);
		QDialogButtonBox* buttons = new QDialogButtonBox(QDialogButtonBox::Save | QDialogButtonBox::Cancel, &dialog);
		QObject::connect(buttons, &QDialogButtonBox::accepted, &dialog, &QDialog::accept);
		QObject::connect(buttons, &QDialogButtonBox::rejected, &dialog, &QDialog::reject);
		layout->addWidget(buttons);
		if (dialog.exec() != QDialog::Accepted)
			return;

		QString mask;
		for (int i = 0; i < 8; i++)
		{
			if (boxes[i]->isChecked())
				mask += QString::number(i + 1);
		}
		const QString dir = QString::fromStdString(Path::Combine(EmuFolders::DataRoot, "reports"));
		QDir().mkpath(dir);
		const QDateTime now = QDateTime::currentDateTime();
		const QString base = QStringLiteral("%1-%2").arg(name.isEmpty() ? QStringLiteral("notes") : name, now.toString(QStringLiteral("yyyyMMdd-HHmmss")));
		QFile md(dir + QDir::separator() + base + QStringLiteral(".md"));
		if (!md.open(QIODevice::WriteOnly | QIODevice::Text))
		{
			QMessageBox::critical(parent, QStringLiteral("RIPPCSX2"), QStringLiteral("Could not write %1").arg(md.fileName()));
			return;
		}
		QTextStream m(&md);
		m << "# " << (name.isEmpty() ? QStringLiteral("Notes") : name) << ": " << result->currentText() << "\n\n";
		m << "- When: " << now.toString(Qt::ISODate) << "\n- Started through: " << loader->currentText() << "\n- OPL modes: " << (mask.isEmpty() ? QStringLiteral("none") : mask) << "\n\n";
		m << notes->toPlainText() << "\n\n## The machine\n\n```\n" << labReport() << "```\n\n## The end of the log\n\n```\n" << logTail(60) << "\n```\n";
		md.close();
		// one row per report, for a script or a spreadsheet to gather
		QFile csv(dir + QDir::separator() + QStringLiteral("compatibility.csv"));
		const bool fresh = !csv.exists();
		if (csv.open(QIODevice::Append | QIODevice::Text))
		{
			QTextStream c(&csv);
			if (fresh)
				c << "when,id,title,crc,started_through,result,opl_modes,video_mode,notes,build\n";
			QString clean = notes->toPlainText();
			clean.replace(QLatin1Char('"'), QStringLiteral("\"\"")).replace(QLatin1Char('\n'), QLatin1Char(' '));
			QString title = QString::fromStdString(VMManager::GetTitle(true));
			title.replace(QLatin1Char('"'), QStringLiteral("\"\""));
			c << now.toString(Qt::ISODate) << ',' << name << ",\"" << title << "\"," << QStringLiteral("%1").arg(VMManager::GetCurrentCRC(), 8, 16, QLatin1Char('0')).toUpper() << ','
			  << loader->currentText().replace(QLatin1Char(','), QLatin1Char(' ')) << ',' << result->currentText().replace(QLatin1Char(','), QLatin1Char(' ')) << ',' << mask << ','
			  << modeName(gsReg(0x10), gsReg(0x20)) << ",\"" << clean << "\"," << BuildVersion::GitRev << "\n";
		}
		if (shot->isChecked() && VMManager::HasValidVM())
		{
			Host::RunOnCPUThread([path = (dir + QDir::separator() + base + QStringLiteral(".png")).toStdString()]() {
				MTGS::RunOnGSThread([path]() { GSQueueSnapshot(path); });
			});
		}
		QMessageBox::information(parent, QStringLiteral("RIPPCSX2"), QStringLiteral("Saved %1 in the reports folder, and added a row to compatibility.csv.").arg(base));
	}

	void runElf(MainWindow* window, const QString& path)
	{
		Host::SetBaseStringSettingValue("RIPPCSX2", "LastELF", path.toUtf8().constData());
		Host::CommitBaseSettingChanges();
		if (!VMManager::HasValidVM())
		{
			window->startFile(path);
			return;
		}
		// one machine at a time: the running one goes first, as a power cycle would
		if (!window->requestShutdown(true, false, false))
			return;
		QTimer* wait = new QTimer(window);
		QObject::connect(wait, &QTimer::timeout, window, [window, wait, path]() {
			if (VMManager::HasValidVM())
				return;
			wait->deleteLater();
			window->startFile(path);
		});
		wait->start(100);
	}

	void applyLabSettings(QWidget* parent, const std::function<void()>& refreshed)
	{
		if (QMessageBox::question(parent, QStringLiteral("RIPPCSX2"),
				QStringLiteral("Set this copy up for testing?\n\n"
							   "EE and IOP console logging on, file logging on, PINE on, the host filesystem on, fast boot on, HDTV output on, "
							   "the EE data write breakpoint on.\n\nYour games, cards and other settings are left alone.")) != QMessageBox::Yes)
		{
			return;
		}
		Host::SetBaseBoolSettingValue("Logging", "EnableEEConsole", true);
		Host::SetBaseBoolSettingValue("Logging", "EnableIOPConsole", true);
		Host::SetBaseBoolSettingValue("Logging", "EnableFileLogging", true);
		Host::SetBaseBoolSettingValue("EmuCore", "EnablePINE", true);
		Host::SetBaseBoolSettingValue("EmuCore", "HostFs", true);
		Host::SetBaseBoolSettingValue("EmuCore", "EnableFastBoot", true);
		Host::SetBaseBoolSettingValue("EmuCore", "DataWriteBreakpoint", true);
		Host::SetBaseBoolSettingValue("EmuCore/GS", "HDTVOutput", true);
		Host::CommitBaseSettingChanges();
		g_emu_thread->applySettings();
		refreshed();
	}
} // namespace

void RIPPCSX2Menu::Install(MainWindow* window, QMenuBar* bar, QMenu* before)
{
	QMenu* menu = new QMenu(QStringLiteral("&RIPPCSX2"), bar);
	menu->setToolTipsVisible(true);
	bar->insertMenu(before->menuAction(), menu);

	auto check = [](QMenu* m, const QString& text, const char* section, const char* key, bool def, const QString& tip) {
		QAction* a = m->addAction(text);
		a->setCheckable(true);
		a->setToolTip(tip);
		SettingWidgetBinder::BindWidgetToBoolSetting(nullptr, a, section, key, def);
		return a;
	};
	auto item = [](QMenu* m, const char* icon, const QString& text, const QString& tip = QString()) {
		QAction* a = m->addAction(QIcon::fromTheme(QString::fromUtf8(icon)), text);
		a->setToolTip(tip);
		return a;
	};

	// ---- run something ----
	QAction* runElfAction = item(menu, "file-line", QStringLiteral("Run &ELF..."), QStringLiteral("Boots an ELF straight away, as a memory card or USB stick would hand it to a PS2."));
	QObject::connect(runElfAction, &QAction::triggered, window, [window]() {
		const QString last = QString::fromStdString(Host::GetBaseStringSettingValue("RIPPCSX2", "LastELF", ""));
		const QString path = QFileDialog::getOpenFileName(window, QStringLiteral("Run ELF"), QFileInfo(last).path(), QStringLiteral("PS2 programs (*.elf *.ELF);;All files (*)"));
		if (!path.isEmpty())
			runElf(window, path);
	});
	QAction* runLast = item(menu, "restart-line", QStringLiteral("Run &Last ELF"), QStringLiteral("The newest build of whatever you ran last: rebuild it, press this, look."));
	QObject::connect(runLast, &QAction::triggered, window, [window]() {
		const QString last = QString::fromStdString(Host::GetBaseStringSettingValue("RIPPCSX2", "LastELF", ""));
		if (!last.isEmpty())
			runElf(window, last);
	});
	menu->addSeparator();

	// ---- see what it does ----
	QObject::connect(item(menu, "chip-line", QStringLiteral("Lab &Monitor..."), QStringLiteral("The video mode and display registers, and the EE data write breakpoint's state, live.")), &QAction::triggered, window, [window]() { showMonitor(window); });
	QObject::connect(item(menu, "list-check", QStringLiteral("&Compatibility Report..."), QStringLiteral("One game's result, the OPL modes used and the machine's state, as a file and a row in compatibility.csv.")), &QAction::triggered, window, [window]() { showReport(window); });
	menu->addSeparator();

	// ---- what it adds to PCSX2 ----
	QAction* hdtv = check(menu, QStringLiteral("&HDTV Output"), "EmuCore/GS", "HDTVOutput", true, QStringLiteral("720p and 1080i shown, captured and saved as an HDTV shows them. Off is stock PCSX2's behaviour, for a side by side."));
	QAction* bp = check(menu, QStringLiteral("EE &Data Write Breakpoint"), "EmuCore", "DataWriteBreakpoint", true, QStringLiteral("The COP0 breakpoint OPL GSM and in-game menus hook the GS with. Off is stock PCSX2's behaviour. Takes effect the next time a program arms it."));

	// ---- lab switches, the same settings the other menus and dialogs use ----
	QMenu* lab = menu->addMenu(QIcon::fromTheme(QStringLiteral("settings-3-line")), QStringLiteral("Lab &Switches"));
	lab->setToolTipsVisible(true);
	QAction* ee = check(lab, QStringLiteral("&EE Console"), "Logging", "EnableEEConsole", false, QStringLiteral("A program's printf from the EE, in the log."));
	QAction* iop = check(lab, QStringLiteral("&IOP Console"), "Logging", "EnableIOPConsole", false, QStringLiteral("The same from the IOP: module loads, driver messages."));
	QAction* logs = check(lab, QStringLiteral("&Log to File"), "Logging", "EnableFileLogging", true, QStringLiteral("logs/emulog.txt"));
	QAction* pine = check(lab, QStringLiteral("&PINE Server"), "EmuCore", "EnablePINE", false, QStringLiteral("Lets a script read and write PS2 memory while it runs."));
	QAction* host = check(lab, QStringLiteral("&Host Filesystem"), "EmuCore", "HostFs", false, QStringLiteral("host: paths reach the folder of the running ELF."));
	QAction* fast = check(lab, QStringLiteral("&Fast Boot"), "EmuCore", "EnableFastBoot", true, QStringLiteral("Straight past the BIOS's intro."));
	lab->addSeparator();
	QObject::connect(item(lab, "settings-3-line", QStringLiteral("Set Up For &Testing...")), &QAction::triggered, window, [window, hdtv, bp, ee, iop, logs, pine, host, fast]() {
		applyLabSettings(window, [=]() {
			for (QAction* a : {hdtv, bp, ee, iop, logs, pine, host, fast})
				a->setChecked(true);
		});
	});

	// ---- where it all lands ----
	QMenu* folders = menu->addMenu(QIcon::fromTheme(QStringLiteral("folder-open-line")), QStringLiteral("Lab &Folders"));
	struct Folder
	{
		QString name;
		const std::string* path;
	};
	const Folder list[] = {{QStringLiteral("&Screenshots"), &EmuFolders::Snapshots}, {QStringLiteral("&Video Captures"), &EmuFolders::Videos}, {QStringLiteral("Save S&tates"), &EmuFolders::Savestates},
		{QStringLiteral("&Memory Cards"), &EmuFolders::MemoryCards}, {QStringLiteral("&Logs"), &EmuFolders::Logs}, {QStringLiteral("&Data Folder"), &EmuFolders::DataRoot}};
	for (const Folder& f : list)
	{
		const std::string* path = f.path;
		QObject::connect(folders->addAction(f.name), &QAction::triggered, window, [window, path]() { openFolder(window, *path); });
	}
	QObject::connect(folders->addAction(QStringLiteral("&Reports")), &QAction::triggered, window, [window]() { openFolder(window, Path::Combine(EmuFolders::DataRoot, "reports")); });
	QObject::connect(item(menu, "file-search-line", QStringLiteral("Open &Log")), &QAction::triggered, window, [window]() { QtUtils::OpenURL(window, QUrl::fromLocalFile(logPath())); });
	menu->addSeparator();

	// ---- about ----
	QObject::connect(item(menu, "global-line", QStringLiteral("RIPPCSX2 &Website...")), &QAction::triggered, window, [window]() { QtUtils::OpenURL(window, SITE_URL); });
	QObject::connect(item(menu, "github", QStringLiteral("RIPPCSX2 on &GitHub...")), &QAction::triggered, window, [window]() { QtUtils::OpenURL(window, REPO_URL); });
	QObject::connect(item(menu, "heart-circle-line", QStringLiteral("&About RIPPCSX2...")), &QAction::triggered, window, [window]() {
		QMessageBox::about(window, QStringLiteral("About RIPPCSX2"),
			QStringLiteral("<b>RIPPCSX2</b>, a PlayStation 2 test and development emulator built on PCSX2.<br><br>"
						   "It runs ELFs, OPL and homebrew the way a console does, shows what they do, and is made to be driven by you or by an AI agent. "
						   "The goal it is working towards: the whole PS2 library running through OPL's own code path, tested and reported.<br><br>"
						   "<a href=\"%1\">%1</a><br><a href=\"%2\">%2</a><br><br>"
						   "An unofficial fork, not affiliated with the PCSX2 team or Sony. Please report problems to the RIPPS2 project, never to PCSX2.").arg(QString::fromUtf8(SITE_URL), QString::fromUtf8(REPO_URL)));
	});

	// what can be pressed depends on what is running and what has been run
	QObject::connect(menu, &QMenu::aboutToShow, window, [runLast]() {
		const QString last = QString::fromStdString(Host::GetBaseStringSettingValue("RIPPCSX2", "LastELF", ""));
		runLast->setEnabled(!last.isEmpty());
		runLast->setText(last.isEmpty() ? QStringLiteral("Run &Last ELF") : QStringLiteral("Run &Last ELF: %1").arg(QFileInfo(last).fileName()));
	});
}

#ifdef _WIN32
namespace
{
	constexpr const wchar_t* PANEL_PREFIX = L"RIPPS2 lab: AI run";

	HWND findPanel()
	{
		HWND found = nullptr;
		EnumWindows([](HWND h, LPARAM out) -> BOOL {
			wchar_t title[64] = {};
			GetWindowTextW(h, title, 64);
			if (wcsncmp(title, PANEL_PREFIX, wcslen(PANEL_PREFIX)) == 0)
			{
				*reinterpret_cast<HWND*>(out) = h;
				return FALSE;
			}
			return TRUE;
		}, reinterpret_cast<LPARAM>(&found));
		return found;
	}

	LRESULT CALLBACK hiddenRunProc(HWND h, UINT msg, WPARAM w, LPARAM l)
	{
		switch (msg)
		{
			case WM_SYSCOMMAND:
				if ((w & 0xFFF0) == SC_RESTORE || (w & 0xFFF0) == SC_MAXIMIZE)
				{
					// it stays a button: pressing it brings up the run's panel, when a driver has one
					if (HWND panel = findPanel())
						SwitchToThisWindow(panel, TRUE);
					return 0;
				}
				break;
			case WM_CLOSE:
				// closing the button stops the run: through the panel when there is one, so the driver hears of it
				if (HWND panel = findPanel())
					PostMessageW(panel, WM_CLOSE, 0, 0);
				else
					QtHost::RunOnUIThread([]() { g_main_window->requestShutdown(false, false, false); });
				return 0;
			case WM_TIMER:
				if (VMManager::HasValidVM())
				{
					const std::wstring title = L"RIPPCSX2 hidden run: " + QString::fromStdString(VMManager::GetTitle(true)).toStdWString();
					SetWindowTextW(h, title.c_str());
				}
				return 0;
			default:
				break;
		}
		return DefWindowProcW(h, msg, w, l);
	}

	BOOL CALLBACK firstIcon(HMODULE mod, LPCWSTR, LPWSTR name, LONG_PTR out)
	{
		*reinterpret_cast<HICON*>(out) = LoadIconW(mod, name);
		return FALSE;
	}

	void hiddenRunThread()
	{
		// a fresh thread can move to another desktop: this one holds the button, the rest of the process stays hidden
		HDESK visible = OpenDesktopW(L"Default", 0, FALSE, DESKTOP_CREATEWINDOW | DESKTOP_CREATEMENU | DESKTOP_READOBJECTS | DESKTOP_WRITEOBJECTS | DESKTOP_ENUMERATE);
		if (!visible || !SetThreadDesktop(visible))
			return;
		HMODULE mod = GetModuleHandleW(nullptr);
		HICON icon = nullptr;
		EnumResourceNamesW(mod, MAKEINTRESOURCEW(14), firstIcon, reinterpret_cast<LONG_PTR>(&icon));
		WNDCLASSEXW wc = {};
		wc.cbSize = sizeof(wc);
		wc.lpfnWndProc = hiddenRunProc;
		wc.hInstance = mod;
		wc.hIcon = icon;
		wc.lpszClassName = L"RIPPCSX2HiddenRun";
		if (!RegisterClassExW(&wc))
			return;
		HWND h = CreateWindowExW(WS_EX_APPWINDOW, wc.lpszClassName, L"RIPPCSX2 hidden run", WS_OVERLAPPEDWINDOW, 0, 0, 240, 120, nullptr, nullptr, mod, nullptr);
		if (!h)
			return;
		ShowWindow(h, SW_SHOWMINNOACTIVE);
		SetTimer(h, 1, 2000, nullptr);
		MSG msg;
		while (GetMessageW(&msg, nullptr, 0, 0) > 0)
		{
			TranslateMessage(&msg);
			DispatchMessageW(&msg);
		}
	}
} // namespace

void RIPPCSX2Menu::StartHiddenRunButton()
{
	static bool s_started = false;
	if (s_started)
		return;
	s_started = true;
	wchar_t name[64] = {};
	DWORD got = 0;
	if (!GetUserObjectInformationW(GetThreadDesktop(GetCurrentThreadId()), UOI_NAME, name, sizeof(name), &got))
		return;
	if (_wcsicmp(name, L"Default") == 0)
		return;
	std::thread(hiddenRunThread).detach();
}
#else
void RIPPCSX2Menu::StartHiddenRunButton()
{
}
#endif
