#!/bin/powershell

$drives = (Get-PSDrive -PSProvider FileSystem).Name 
Foreach-Object { Optemize-Volume -DriveLetter $drives -Defrag -Verbose }
