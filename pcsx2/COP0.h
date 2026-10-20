// SPDX-FileCopyrightText: 2002-2026 PCSX2 Dev Team
// SPDX-License-Identifier: GPL-3.0+

#pragma once

struct tlbs;

extern void WriteCP0Status(u32 value);
extern void WriteCP0Config(u32 value);
extern void cpuUpdateOperationMode();
extern void WriteTLB(int i);
extern void UnmapTLB(const tlbs& t, int i);
extern void MapTLB(const tlbs& t, int i);

extern void COP0_UpdatePCCR();
extern void COP0_DiagnosticPCCR();

// RIPPCSX2: the R5900 hardware breakpoint registers (COP0 $24: MTBPC/MTDAB/MTDABM...) and the data
// write breakpoint they arm. Only data WRITE breakpoints raise the debug exception (level 2, vector
// 0x80000100, ErrorEPC + Cause.BD2), which is what OPL/RIPPS2 GSM's GSHandler needs for the GS
// privileged registers. Instruction and data read/value breakpoints are stored but never fire.
struct EEDebugRegs
{
	u32 BPC, IAB, IABM, DAB, DABM, DVB, DVBM;
};
extern EEDebugRegs eeDebugRegs;
// Runtime compare used by the interpreter and the recompiled code: a store at addr traps when
// (addr & eeDataWriteBpMask) == eeDataWriteBpMatch. Mask 0 / match 1 never matches (trap not live
// in the current CPU mode).
extern u32 eeDataWriteBpMask;
extern u32 eeDataWriteBpMatch;
extern bool eeDataWriteBpArmed();
extern void eeDebugRegsUpdate();
extern void eeDebugRegsReset();
extern u32 ReadCP0Debug(u32 sel);
extern void WriteCP0Debug(u32 sel, u32 value);
extern void eeDataWriteBpException(u32 storepc, u32 bd);
