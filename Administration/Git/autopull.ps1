#!/bin/env powershell

Get-ChildItem -Path ~\Git\ -Name | 
Select-String -Pattern ".secrets" -NotMatch | 
Select-String -Pattern "autopull.ps1" -NotMatch | 
Select-String -Pattern ".git" -NotMatch | 
ForEach-Object {cd $_; git pull; cd ..}
