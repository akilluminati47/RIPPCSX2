# Puts a RIPPCSX2 build (the CI artifact, as its .zip or unzipped) into the RIPPS2 lab's portable PCSX2, keeping the
# lab's own files: settings, memory cards, captures, screenshots, save states, caches and logs. The binaries it
# replaces go to a dated folder beside the lab first, so a build can be taken back.
#
#   .\install-lab.ps1 -Build C:\Downloads\RIPPCSX2-windows-x64-avx2-sha[1a2b3c4].zip [-Lab B:\...\ripps2-lab]
param(
  [Parameter(Mandatory = $true)][string]$Build,
  [string]$Lab = "B:\Emulation\PlayStation\PCSX2\ripps2-lab"
)
$ErrorActionPreference = "Stop"

# the lab's own files and folders: never overwritten, never moved
$keep = @("inis", "memcards", "videos", "snaps", "sstates", "cache", "covers", "logs", "gamesettings", "cheats",
  "patches", "inputprofiles", "textures", "debuggerlayouts", "debuggersettings", "portable.txt")

if (-not (Test-Path -LiteralPath $Lab)) { throw "No lab at $Lab" }
$running = Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.Path -and $_.Path.StartsWith($Lab, [StringComparison]::OrdinalIgnoreCase) }
if ($running) { throw "The lab PCSX2 is running ($($running[0].Name)); close it first." }

$src = (Resolve-Path -LiteralPath $Build).Path
$unzipped = $null
if ($src -like "*.zip") {
  $unzipped = Join-Path $env:TEMP ("rippcsx2-" + [guid]::NewGuid().ToString("N"))
  Expand-Archive -LiteralPath $src -DestinationPath $unzipped
  $src = $unzipped
}
# the artifact may hold the build at its root or one folder down
$exe = Get-ChildItem -LiteralPath $src -Filter "pcsx2-qt*.exe" -File -Recurse | Sort-Object { $_.FullName.Length } | Select-Object -First 1
if (-not $exe) { throw "No pcsx2-qt*.exe in $Build" }
$root = $exe.DirectoryName

# back up what will be replaced
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$backup = Join-Path (Split-Path -Parent $Lab) ("ripps2-lab-binaries-" + $stamp)
New-Item -ItemType Directory -Path $backup | Out-Null
Get-ChildItem -LiteralPath $Lab | Where-Object { $keep -notcontains $_.Name } | ForEach-Object {
  Copy-Item -LiteralPath $_.FullName -Destination $backup -Recurse -Force
}

# copy the build in, skipping anything that would land on the lab's own files
Get-ChildItem -LiteralPath $root | Where-Object { $keep -notcontains $_.Name } | ForEach-Object {
  Copy-Item -LiteralPath $_.FullName -Destination $Lab -Recurse -Force
}
# the lab's driver (ps2bg.ps1) starts pcsx2-qt.exe; MSBuild may name it pcsx2-qtx64-avx2.exe
if ($exe.Name -ne "pcsx2-qt.exe") {
  Copy-Item -LiteralPath (Join-Path $Lab $exe.Name) -Destination (Join-Path $Lab "pcsx2-qt.exe") -Force
}
if (-not (Test-Path -LiteralPath (Join-Path $Lab "portable.txt"))) { New-Item -ItemType File -Path (Join-Path $Lab "portable.txt") | Out-Null }

# HDTVOutput defaults on; say so if the lab's settings turned it off
$ini = Join-Path $Lab "inis\PCSX2.ini"
if ((Test-Path -LiteralPath $ini) -and (Select-String -LiteralPath $ini -Pattern "^HDTVOutput\s*=\s*false" -Quiet)) {
  Write-Warning "inis\PCSX2.ini has HDTVOutput = false: HD modes will look as in stock PCSX2."
}
if ($unzipped) { Remove-Item -LiteralPath $unzipped -Recurse -Force }

$v = (Get-Item -LiteralPath (Join-Path $Lab "pcsx2-qt.exe")).VersionInfo.ProductVersion
"Installed $($exe.Name) ($v) into $Lab; the old binaries are in $backup"
