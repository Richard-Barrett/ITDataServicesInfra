#!/bin/powershell
(Get-PSDrive -PSProvider FileSystem).Name |
Foreach-Object { Optemize-Volume -DriveLetter $_ -Defrag -Verbose }
