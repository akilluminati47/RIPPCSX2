// SPDX-FileCopyrightText: 2002-2026 PCSX2 Dev Team
// SPDX-License-Identifier: GPL-3.0+

#pragma once

class MainWindow;
class QMenuBar;
class QMenu;

/// RIPPCSX2: the fork's own menu, between Debug and Help, built like the menus beside it. Every tool the fork has added
/// and every switch a lab run needs, in one place. Not in upstream PCSX2.
namespace RIPPCSX2Menu
{
	/// Adds the menu to the bar, ahead of `before`. Called each time the main window sets up its UI.
	void Install(MainWindow* window, QMenuBar* bar, QMenu* before);

	/// When this process was started on a hidden desktop, puts one small button on the visible desktop's taskbar. It belongs
	/// to this process, so whatever acts on an app through its taskbar button (a per-app volume mod, say) reaches this PCSX2.
	void StartHiddenRunButton();
} // namespace RIPPCSX2Menu
