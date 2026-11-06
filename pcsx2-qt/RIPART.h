// SPDX-FileCopyrightText: 2002-2026 PCSX2 Dev Team
// SPDX-License-Identifier: GPL-3.0+

#pragma once

class QWidget;

/// RIPART: OPL Manager's art database for themers and libraries. Decoy game entries so a theme can be judged on real art with
/// no games on the drive, a checkbox list of every game with each piece of art to choose from, a scan for games on a drive with
/// no art, and an ART folder or an art.tar to put them in. Not in upstream PCSX2.
namespace RIPART
{
	/// The tool's window, modal to `parent`.
	void Open(QWidget* parent);
} // namespace RIPART
