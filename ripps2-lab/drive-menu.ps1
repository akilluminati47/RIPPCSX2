# Drives a private RIPPCSX2 on a hidden desktop of its own: launches it, sends clicks and keys by window message, grabs every window it shows.
# Nothing takes the focus and the keyboard and mouse stay yours.
# drive-menu.ps1 -Lab <folder> -Exe <exe> -Actions "wait:16,move:274:11,wait:0.3,click:274:11,wait:0.8,popkey:40,popkey:40,popkey:13,wait:2,list,grab:monitor" [-ElfArg path] [-Out folder] [-Keep]
# wait:<s>, list, grab:<name>, click:<x>:<y> and move:<x>:<y> in the main window, pop:<x>:<y> in the newest other window, key:<vk>, popkey:<vk>.
# (274, 11) is the RIPPCSX2 menu's title. Inside a popup menu use the keys: a posted click closes it without choosing. 40 down, 39 right, 13 enter.
param([string]$Lab = ".", [string]$Exe = "pcsx2-qtx64-avx2.exe", [string]$Actions = "wait:6,grab:start", [string]$ElfArg = "", [string]$Out = ".\menu-grabs", [switch]$Keep)
New-Item -ItemType Directory -Force $Out | Out-Null
Add-Type -AssemblyName System.Drawing
Add-Type -ReferencedAssemblies System.Drawing @"
using System; using System.Collections.Generic; using System.Runtime.InteropServices; using System.Text;
public static class T {
  [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)] public struct STARTUPINFO { public int cb; public string lpReserved, lpDesktop, lpTitle; public int dwX, dwY, dwXSize, dwYSize, dwXCountChars, dwYCountChars, dwFillAttribute, dwFlags; public short wShowWindow, cbReserved2; public IntPtr lpReserved2, hStdInput, hStdOutput, hStdError; }
  [StructLayout(LayoutKind.Sequential)] public struct PROCESS_INFORMATION { public IntPtr hProcess, hThread; public int dwProcessId, dwThreadId; }
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, Tp, R, B; }
  [DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)] static extern bool CreateProcess(string app, StringBuilder cmd, IntPtr pa, IntPtr ta, bool inherit, uint flags, IntPtr env, string dir, ref STARTUPINFO si, out PROCESS_INFORMATION pi);
  public delegate bool EnumProc(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc f, IntPtr l);
  [DllImport("user32.dll")] static extern bool EnumDesktopWindows(IntPtr d, EnumProc f, IntPtr l);
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern bool IsIconic(IntPtr h);
  [DllImport("user32.dll")] public static extern int GetWindowLong(IntPtr h, int i);
  [DllImport("user32.dll", CharSet = CharSet.Unicode)] static extern int GetClassName(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll", CharSet = CharSet.Unicode)] static extern int GetWindowText(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll")] public static extern bool PostMessage(IntPtr h, uint m, IntPtr w, IntPtr l);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  [DllImport("user32.dll")] static extern bool GetClientRect(IntPtr h, out RECT r);
  [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr h, IntPtr dc, uint f);
  [DllImport("user32.dll", CharSet = CharSet.Unicode)] static extern IntPtr CreateDesktop(string n, IntPtr d, IntPtr m, int f, uint a, IntPtr s);
  [DllImport("user32.dll", CharSet = CharSet.Unicode)] static extern IntPtr OpenDesktop(string n, int f, bool i, uint a);
  [DllImport("user32.dll")] static extern bool SetThreadDesktop(IntPtr h);
  public static string Name = "RIPPCSX2TEST"; public static IntPtr Desk;
  public static void Open() { Desk = OpenDesktop(Name, 0, false, 0x10000000); if (Desk == IntPtr.Zero) Desk = CreateDesktop(Name, IntPtr.Zero, IntPtr.Zero, 0, 0x10000000, IntPtr.Zero); }
  static void On(Action f) { Exception e = null; var t = new System.Threading.Thread(() => { try { SetThreadDesktop(Desk); f(); } catch (Exception x) { e = x; } }); t.Start(); t.Join(); if (e != null) throw e; }
  public static int Launch(string exe, string args, string dir) {
    var si = new STARTUPINFO(); si.cb = Marshal.SizeOf(si); si.dwFlags = 1; si.wShowWindow = 1; si.lpDesktop = "WinSta0\\" + Name; PROCESS_INFORMATION pi;
    if (!CreateProcess(exe, new StringBuilder("\"" + exe + "\" " + args), IntPtr.Zero, IntPtr.Zero, false, 0, IntPtr.Zero, dir, ref si, out pi)) return -1; return pi.dwProcessId; }
  public static string Info(IntPtr h) { var c = new StringBuilder(128); GetClassName(h, c, 128); var t = new StringBuilder(128); GetWindowText(h, t, 128); RECT r; GetWindowRect(h, out r); return c + " '" + t + "' " + (r.R - r.L) + "x" + (r.B - r.Tp) + " at " + r.L + "," + r.Tp; }
  public static List<IntPtr> Windows(int pid) { var list = new List<IntPtr>(); On(() => EnumDesktopWindows(Desk, (h, l) => { uint p; GetWindowThreadProcessId(h, out p); if (p == pid && IsWindowVisible(h)) { RECT r; GetWindowRect(h, out r); if (r.R - r.L > 20 && r.B - r.Tp > 12) list.Add(h); } return true; }, IntPtr.Zero)); return list; }
  public static List<IntPtr> VisibleDesktopWindows(int pid) { var list = new List<IntPtr>(); EnumWindows((h, l) => { uint p; GetWindowThreadProcessId(h, out p); if (p == pid) list.Add(h); return true; }, IntPtr.Zero); return list; }
  public static void Grab(IntPtr h, string file) { On(() => { RECT r; GetWindowRect(h, out r); int w = r.R - r.L, hh = r.B - r.Tp; if (w <= 0 || hh <= 0) return; using (var b = new System.Drawing.Bitmap(w, hh)) { using (var g = System.Drawing.Graphics.FromImage(b)) { var dc = g.GetHdc(); PrintWindow(h, dc, 2); g.ReleaseHdc(dc); } b.Save(file, System.Drawing.Imaging.ImageFormat.Png); } }); }
  public static void Click(IntPtr h, int x, int y) { On(() => { var l = (IntPtr)((y << 16) | (x & 0xffff)); PostMessage(h, 0x0200, IntPtr.Zero, l); System.Threading.Thread.Sleep(60); PostMessage(h, 0x0201, (IntPtr)1, l); System.Threading.Thread.Sleep(60); PostMessage(h, 0x0202, IntPtr.Zero, l); }); }
  public static void Move(IntPtr h, int x, int y) { On(() => { var l = (IntPtr)((y << 16) | (x & 0xffff)); PostMessage(h, 0x0200, IntPtr.Zero, l); }); }
  public static void Key(IntPtr h, int vk) { On(() => { PostMessage(h, 0x0100, (IntPtr)vk, (IntPtr)1); System.Threading.Thread.Sleep(40); PostMessage(h, 0x0101, (IntPtr)vk, unchecked((IntPtr)0xC0000001)); }); }
  public static void Close(IntPtr h) { On(() => PostMessage(h, 0x0010, IntPtr.Zero, IntPtr.Zero)); }
}
"@
$lab = (Resolve-Path $Lab).Path
[T]::Open()
$args0 = if ($ElfArg) { "-fastboot -elf `"$ElfArg`"" } else { "" }
$procId = [T]::Launch("$lab\$Exe", $args0, $lab)
"launched $procId"
$p = Get-Process -Id $procId
function Main { $best = [IntPtr]::Zero; $area = 0; foreach ($h in [T]::Windows($procId)) { $r = New-Object T+RECT; [void][T]::GetWindowRect($h, [ref]$r); $a = ($r.R - $r.L) * ($r.B - $r.Tp); if ($a -gt $area) { $area = $a; $best = $h } }; return $best }
$top = @()
foreach ($s in ($Actions -split ',')) {
  $a = $s.Split(':')
  switch ($a[0]) {
    'wait' { Start-Sleep -Milliseconds ([double]$a[1] * 1000) }
    'list' { "--- windows on the hidden desktop"; foreach ($h in [T]::Windows($procId)) { "  $h " + [T]::Info($h) }; "--- this process's windows on the visible desktop"; foreach ($h in [T]::VisibleDesktopWindows($procId)) { "  $h visible=" + [T]::IsWindowVisible($h) + " iconic=" + [T]::IsIconic($h) + " exstyle=0x" + ([T]::GetWindowLong($h, -20)).ToString('x') + " " + [T]::Info($h) } }
    'grab' { $i = 0; foreach ($h in [T]::Windows($procId)) { $f = Join-Path $Out ("{0}_{1}.png" -f $a[1], $i); [T]::Grab($h, $f); "grab $f " + [T]::Info($h); $i++ } }
    'click' { [T]::Click((Main), [int]$a[1], [int]$a[2]) }
    'move' { [T]::Move((Main), [int]$a[1], [int]$a[2]) }
    # clicks in the newest small window: a popup menu or a dialog
    'pop' { $ws = [T]::Windows($procId); $m = Main; $hit = $null; foreach ($h in $ws) { if ($h -ne $m) { $hit = $h; break } }; if ($hit) { [T]::Move($hit, [int]$a[1], [int]$a[2]); Start-Sleep -Milliseconds 120; [T]::Click($hit, [int]$a[1], [int]$a[2]); "pop clicked " + [T]::Info($hit) } else { "no popup" } }
    'key' { [T]::Key((Main), [int]$a[1]) }
    'popkey' { $ws = [T]::Windows($procId); $m = Main; foreach ($h in $ws) { if ($h -ne $m) { [T]::Key($h, [int]$a[1]); break } } }
    default { "unknown $s" }
  }
}
if (-not $Keep) {
  foreach ($h in [T]::Windows($procId)) { [T]::Close($h) }
  Start-Sleep -Seconds 2
  try { if (-not $p.HasExited) { Stop-Process -Id $procId -Force } } catch {}
  "closed"
}
