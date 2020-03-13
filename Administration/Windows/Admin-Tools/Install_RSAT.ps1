#!/bin/powershell

Add-WindowsCapability –online –Name "Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0"
Install-WindowsFeature -Name "RSAT-AD-PowerShell" –IncludeAllSubFeature
