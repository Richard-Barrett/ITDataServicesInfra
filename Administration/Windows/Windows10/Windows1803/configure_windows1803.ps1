#!/bin/powershell

# Call Chocolatey Install for Packages
cd .\Git\ITDataServicesInfra\Administration\Windows\Chocolatey\Packages\

# Run Powershell Script 
.\Choco_Server_Packages.ps1

# Install RSAT and Enable Hyper-V
Install-WindowsFeature -Name "RSAT-AD-PowerShell" –IncludeAllSubFeature
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
