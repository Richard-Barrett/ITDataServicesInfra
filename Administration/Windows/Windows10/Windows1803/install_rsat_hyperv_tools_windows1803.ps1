#!/bin/powershell

# Install RSAT and Enable Hyper-V
Install-WindowsFeature -Name "RSAT-AD-PowerShell" –IncludeAllSubFeature
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V
