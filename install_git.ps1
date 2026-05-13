# Script pour installer Git
$progressPreference = 'silentlyContinue'
$url = 'https://github.com/git-for-windows/git/releases/download/v2.45.0.windows.1/Git-2.45.0-64-bit.exe'
$output = "$env:TEMP\GitInstaller.exe"

Write-Host 'Telecharger Git...'
Invoke-WebRequest -Uri $url -OutFile $output

Write-Host 'Installation de Git...'
& $output /SILENT /NORESTART

Write-Host 'Git installe avec succes!'
