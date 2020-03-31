#!/bin/powershell

# Initialize git pull recursively
Get-ChildItem -Path ~\Git\ -Name | Select-String -Pattern ".secrets" -NotMatch | ForEach-Object {cd $_; git pull; cd ..}
