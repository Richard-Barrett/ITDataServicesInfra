# Find the Realtek Audio Legacy HDA driver integration *** Does not apply to the new UAD drivers ***
# Version 1.3 / 10-Jan-2020. (c) Dimitri Delopoulos
# 1.0:   Initial release
# 1.1:   Added Identification of Audio CODEC (Thanks to Cliff S for the suggestion)
# 1.2:   Fixed detection of Realtek Audio CODEC ALC1150
#        Updated special files to driver version 6.0.1.8648 and higher
#        Added 32-bit version compatibility
# 1.2.1: Fixed detection of Realtek Audio CODEC ALC898
# 1.3:   Fixed detection of multiple integrations
#        Added INF file required for installation


### Get HardwareID
$HWID = (Get-CimInstance Win32_PnPSignedDriver | where {$_.DriverProviderName -Match 'Realtek' -and $_.DeviceClass -match 'MEDIA'} -ErrorAction SilentlyContinue).HardWareID

if ( [string]::IsNullOrEmpty($HWID) ) {
    Write-Host "`nThe Audio device is not controlled by a Realtek driver.`n" -ForegroundColor Red
    Remove-Variable HWID     # Cleanup before exiting
    Exit
    }

$CODEC_ID = $HWID.Substring($HWID.IndexOf('DEV_')+4, 4)

$CODEC = switch ( $CODEC_ID )
    {
    '0899' { '898';  break }
    '0900' { '1150'; break }
    default { $CODEC_ID.TrimStart('0') }
    }

### Get Realtek Driver
$Driver = Get-WindowsDriver -Online | where {$_.ProviderName -Match 'Realtek' -and $_.ClassName -match 'MEDIA'} | sort Date | select -Last 1 -ErrorAction SilentlyContinue
$DriverVersion = $Driver.Version
$DriverInf = Split-Path -Path $Driver.OriginalFileName -Leaf

Write-Host "`nAudio device Hardware ID: " -NoNewline
Write-Host $HWID -ForegroundColor Magenta
Write-Host "$("Realtek Audio CODEC".PadRight(24)): " -NoNewline
Write-Host "ALC$CODEC" -ForegroundColor Magenta

### Get OS Architecture
if ([Environment]::Is64BitOperatingSystem) { $OS = "WIN64" }
else { $OS = "WIN32" }

### Get System OEM
$OEM = (Get-CimInstance -ClassName Win32_BaseBoard).Manufacturer
if ( [string]::IsNullOrEmpty($OEM) ) { $OEM = "OEM" }

### Define Integrations
$FF01Name = "FF01"
$FF01Description = "Fortemedia (FMAPO) Integration"
if ($OS -eq 'WIN64') { $FF01 = @("FMAPO32.dll", "FMAPO64.dll", "FMAPP.dll", "FMAPP.exe") }
else { $FF01 = @("FMAPO.dll", "FMAPP.dll", "FMAPP.exe") }

$FF03Name = "FF03"
$FF03Description = "Nahimic Integration"
if ($OS -eq 'WIN64') { $FF03 = @("NAHIMICAPOlfx.dll", "NahimicAPONSControl.dll", "NAHIMICV2apo.dll", "NAHIMICV3apo.dll") }
else { $FF03 = @("NAHIMICAPOlfx.dll", "NahimicAPONSControl.dll", "NAHIMICV2apo.dll", "NAHIMICV3apo.dll") }

$FF04Name = "FF04"
$FF04Description = "Conexant (CXAPO) Integration"
if ($OS -eq 'WIN64') {
    $FF04 = @("Caf64api.dll", "CAF64APO2.dll", "CX32APO.dll", "CX64APO.dll", "CX64Proxy.dll", "cxapo.lncs", 
              "cxapo.prop", "CXAPOAgent64.exe") }
else  { $FF04 = @("Caf32api.dll", "Caf32APO2.dll", "CX32APO.dll", "CX32Proxy.dll", "cxapo.lncs", 
                  "cxapo.prop", "CXAPOAgent.exe") }

$FF06Name = "FF06"
$FF06Description = "MaxxAudio Integration"
if ($OS -eq 'WIN64') {
    $FF06 = @("MaxxAudioAPO20.dll", "MaxxAudioAPO30.dll", "MaxxAudioAPO4064.dll", "MaxxAudioAPO5064.dll", 
              "MaxxAudioAPO6064.dll", "MaxxAudioAPO7064.dll", "MaxxAudioAPOShell64.dll", "MaxxAudioCapture64.dll", 
              "MaxxAudioEQ64.dll", "MaxxAudioMeters64.exe", "MaxxAudioRealtek64.dll", "MaxxAudioRender64.dll", 
              "MaxxAudioRenderAVX64.dll", "MaxxAudioVienna264.dll", "MaxxSpeechAPO.dll", "MaxxSpeechAPO64.dll", 
              "MaxxVoiceAPO2064.dll", "MaxxVoiceAPO30.dll", "MaxxVoiceAPO3064.dll", "MaxxVoiceAPO4064.dll", 
              "MaxxVolumeSDAPO.dll", "tbb_waves.dll", "WavesGUILib64.dll") }
else { 
    $FF06 = @("MaxxAudioAPO.dll", "MaxxAudioAPO20.dll", "MaxxAudioAPO30.dll", "MaxxAudioAPO40.dll",
              "MaxxAudioAPO50.dll", "MaxxAudioAPO60.dll", "MaxxAudioAPO70.dll", "MaxxAudioAPOShell.dll",
              "MaxxAudioCapture.dll", "MaxxAudioEQ.dll", "MaxxAudioMeters.exe", "MaxxAudioRealtek.dll",
              "MaxxAudioRender.dll", "MaxxAudioRenderAVX.dll", "MaxxAudioVienna2.dll", "MaxxSpeechAPO.dll",
              "MaxxVoiceAPO20.dll", "MaxxVoiceAPO30.dll", "MaxxVoiceAPO40.dll", "MaxxVolumeSDAPO.dll",
              "tbb_waves.dll", "WavesGUILib.dll", "WavesLib.dll") } 

$FF10Name = "FF10"
$FF10Description = "Creative Integration"
if ($OS -eq 'WIN64') {
    $FF10 = @("GWfilt64.sys", "MBAPO232.dll", "MBAPO264.dll", "MBAPO32.dll", "MBAPO64.dll", "mbfilt64.sys", 
              "MBPPCn64.dll", "MBppld64.dll", "MBTHX32.dll", "MBTHX64.dll", "MBWrp64.dll") }
else { $FF10 = @("MBAPO232.dll", "MBAPO32.dll", "mbfilt32.sys", "MBPPCn32.dll", "MBppld32.dll",
                 "MBTHX32.dll", "MBWrp32.dll") }

$FF0CName = "FF0C"
$FF0CDescription = "Intel (DTS/SST) Integration"
if ($OS -eq 'WIN64') {
    $FF0C = @("IntelSSTAPO.dll", "IntelSSTAPO_FF.dll", "IntelSstCApoPropPage.dll", "IntelSSTPreproc_v124.dll",
          "rtkSSTsetting.dat", "rtkSSTsettingFF.dat") }
else { $FF0C = @() }

### Check existing Integrations
$DriverIntegration = @()
$Integrations = @()

$FF01 | ForEach-Object { $DriverIntegration += Get-ChildItem -Path (Split-Path $Driver.OriginalFileName) $_ }
$FF01Log = $DriverIntegration     #Debug Information
if ($DriverIntegration -ne $null) {
    $DriverIntegrationName = $FF01Name
    $DriverIntegrationDescription = $FF01Description
    $DriverIntegration = @()
    $Integrations += $FF01Name
    }

$FF03 | ForEach-Object { $DriverIntegration += Get-ChildItem -Path (Split-Path $Driver.OriginalFileName) $_ }
$FF03Log = $DriverIntegration     #Debug Information
if ($DriverIntegration -ne $null) {
    $DriverIntegrationName = $FF03Name
    $DriverIntegrationDescription = $FF03Description
    $DriverIntegration = @()
    $Integrations += $FF03Name
    }

$FF04 | ForEach-Object { $DriverIntegration += Get-ChildItem -Path (Split-Path $Driver.OriginalFileName) $_ }
$FF04Log = $DriverIntegration     #Debug Information
if ($DriverIntegration -ne $null) {
    $DriverIntegrationName = $FF04Name
    $DriverIntegrationDescription = $FF04Description
    $DriverIntegration = @()
    $Integrations += $FF04Name
    }

$FF06 | ForEach-Object { $DriverIntegration += Get-ChildItem -Path (Split-Path $Driver.OriginalFileName) $_ }
$FF06Log = $DriverIntegration     #Debug Information
if ($DriverIntegration -ne $null) {
    $DriverIntegrationName = $FF06Name
    $DriverIntegrationDescription = $FF06Description
    $DriverIntegration = @()
    $Integrations += $FF06Name
    }

$FF10 | ForEach-Object { $DriverIntegration += Get-ChildItem -Path (Split-Path $Driver.OriginalFileName) $_ }
$FF10Log = $DriverIntegration     #Debug Information
if ($DriverIntegration -ne $null) {
    $DriverIntegrationName = $FF10Name
    $DriverIntegrationDescription = $FF10Description
    $DriverIntegration = @()
    $Integrations += $FF10Name
    }

$FF0C | ForEach-Object { $DriverIntegration += Get-ChildItem -Path (Split-Path $Driver.OriginalFileName) $_ }
$FF0CLog = $DriverIntegration     #Debug Information
if ($DriverIntegration -ne $null) {
    $DriverIntegrationName = $FF0CName
    $DriverIntegrationDescription = $FF0CDescription
    $DriverIntegration = @()
    $Integrations += $FF0CName
    }

if ($Integrations.Length -eq 0) {
    $DriverIntegrationName = "FF00"
    $DriverIntegrationDescription = "No Integration (Generic)"
    }
elseif ($Integrations.Length -gt 1) { 
    $DriverIntegrationName = "$OEM specific"
    $DriverIntegrationDescription = "Multiple Integrations"
    $OutputIntegrations = -join ("[", ($Integrations -join '-').trim(), "]")
    }

### Output on screen
Write-Host "`nThe Audio device is controlled by Realtek Audio driver version " -NoNewline
Write-Host $DriverVersion -NoNewline -ForegroundColor Green
Write-Host " with " -NoNewline
Write-Host $DriverIntegrationDescription -ForegroundColor Cyan -NoNewline
if ($Integrations.Length -gt 1) { Write-Host " $OutputIntegrations" -NoNewline -ForegroundColor Cyan }
Write-Host "`r"
Write-Host "Proposed legacy HDA driver : " -NoNewline
if ($Integrations.Length -gt 1) { Write-Host "Customized " -ForegroundColor Cyan -NoNewline }
Write-Host $DriverIntegrationName -ForegroundColor Cyan -NoNewline
Write-Host "`r"
Write-Host "INF needed for installation: " -NoNewline 
Write-Host "$DriverInf`n" -ForegroundColor Cyan

### Log Information
$LogFile = "$env:USERPROFILE\Desktop\RealtekAudioDriverIntegration.log"
Get-ChildItem $LogFile -ErrorAction SilentlyContinue | Remove-Item -Force -ErrorAction SilentlyContinue
New-Item $LogFile -ItemType File | Out-Null
Set-Content $LogFile "Realtek Audio Driver Integration log information" -Encoding Unicode

"`nDevice HWID: $HWID`nAudio CODEC: ALC$CODEC`n
Realtek Driver Version: $DriverVersion
HDA Driver Integration: $DriverIntegrationName - $DriverIntegrationDescription
INF needed to install : $DriverInf`n" | 
Out-File $LogFile -Append unicode

Out-File $LogFile -Append -InputObject ("-"*55 + "`n" + "$FF01Name - $FF01Description" + "`n" + "-"*55 + "`n" + ($FF01Log -join "`n") + "`n") unicode
Out-File $LogFile -Append -InputObject ("-"*55 + "`n" + "$FF03Name - $FF03Description" + "`n" + "-"*55 + "`n" + ($FF03Log -join "`n") + "`n") unicode
Out-File $LogFile -Append -InputObject ("-"*55 + "`n" + "$FF04Name - $FF04Description" + "`n" + "-"*55 + "`n" + ($FF04Log -join "`n") + "`n") unicode
Out-File $LogFile -Append -InputObject ("-"*55 + "`n" + "$FF06Name - $FF06Description" + "`n" + "-"*55 + "`n" + ($FF06Log -join "`n") + "`n") unicode
Out-File $LogFile -Append -InputObject ("-"*55 + "`n" + "$FF10Name - $FF10Description" + "`n" + "-"*55 + "`n" + ($FF10Log -join "`n") + "`n") unicode
Out-File $LogFile -Append -InputObject ("-"*55 + "`n" + "$FF0CName - $FF0CDescription" + "`n" + "-"*55 + "`n" + ($FF0CLog -join "`n") + "`n") unicode

### Cleanup before exiting
Remove-Variable HWID, CODEC_ID,CODEC, Driver, DriverVersion, DriverInf, OS, OEM, FF01, FF01Name, FF01Description, FF03, FF03Name, FF03Description, 
                FF04, FF04Name, FF04Description,FF06, FF06Name, FF06Description, FF10, FF10Name ,FF10Description,  FF0C, FF0CName, FF0CDescription, 
                DriverIntegration, DriverIntegrationDescription, DriverIntegrationName, Integrations, OutputIntegrations, 
                FF01Log, FF03Log, FF04Log, FF06Log, FF10Log, FF0CLog, LogFile -ErrorAction SilentlyContinue
