#!/bin/powershell

# Installs All Packages 
# Packages that need to be installed for server work on Server Machine 
cat .\Server_Packages.txt | ForEach-Object { choco install $_ -y}
