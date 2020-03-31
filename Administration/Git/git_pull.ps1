#!/bin/powershell

# Initialize git pull recursively
Get-ChildItem -Path C:\Users\richard.barrett\Git\ -Name | Select-String -Pattern ".secrets" -NotMatch | ForEach-Object {cd $_; git pull; cd ..}
