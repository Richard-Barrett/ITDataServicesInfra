## Administration
This section contains overall administrative scripts to get started with working with the repository. 
In here there are scripts that will set up automated tasks like Git Pulls, Package Installations, and overall Administrative tasks required by a Sysadmin to get started. 

# Git
This directory contains two scripts. 
The two scripts are to refresh the repository for both Windows and Linux machines. 
- **[Linux Git Pull](https://github.com/Richard-Barrett/ITDataServicesInfra/blob/master/Administration/Git/git_pull.sh)**
- **[Windows Git Pull](https://github.com/Richard-Barrett/ITDataServicesInfra/blob/master/Administration/Git/git_pull.ps1)**

What this does is it allows you to set up an auotmated schedule pull of the repository. 
If at any time you want to refresh your clone of the repository you can instantiate a **`git pull`**

**For Linux:**
```bash
cd ~/Git/ITDataServicesInfra &&  git pull
```

**For Windows:**
```powershell
cd ~\Git\ITDataServicesInfra ; git pull
```
# Linux
This section contains administrative scripts to get started across the various flavors of Linux. 
The scripts range from Installation, Administration, an Provisioning the Initial Setup of a Linux Desktop and/or Server.
The Current Release contains the following Directories and Sub-Directories.
```powershell
PS C:\Users\richard.barrett\Git\ITDataServicesInfra\Administration\Linux> tree
Folder PATH listing for volume OS
Volume serial number is 1E07-4DEE
C:.
├───CentOS
│   ├───CentOS6
│   ├───CentOS7
│   └───CentOS8
├───Debian
│   ├───Fedora
│   ├───Kalilinux
│   └───ParrotOS
├───Flavors
│   ├───CentOS7
│   ├───CentOS8
│   ├───Ubuntu1604
│   ├───Ubuntu1804
│   └───Ubuntu1904
├───RHEL
└───Ubuntu
    ├───14.04
    ├───16.04
    ├───18.04
    └───19.04
```
# macOS
This section contains administrative scripts to get started across the various versions of macOS. 
The scripts range from Installation, Administration, an Provisioning the Initial Setup of a macOS Desktop.
The Current Release contains the following Directories and Sub-Directories.
```
└── macOS
    ├── Catalina
    │   └── README.md
    ├── HighSierra
    │   └── README.md
    ├── Mojave
    │   └── README.md
    ├── README.md
    └── Sierra
        └── README.md
```

# Windows
This section contains scripts use for setting up the repository on a windows based machine. 
It will allow you to work across a variety of versions including Windows 2016 and versions of Windows 10 1803+. 
The current release has the following information in regards to Directories and SUb-Directories.
```powershell
PS C:\Users\richard.barrett\Git\ITDataServicesInfra\Administration\Windows> tree
Folder PATH listing for volume OS
Volume serial number is 1E07-4DEE
C:.
├───Admin-Tools
├───Chocolatey
│   ├───Packages
│   └───Security
├───Windows-Server2016
├───Windows-Server2019
└───Windows10
    ├───Windows1803
    ├───Windows1903
    └───WindowsIP
```

Documentation and Articles for Windows Administration:
- **[Installing AD RSAT Tool and Pulling Out Email and User Information](http://woshub.com/get-aduser-getting-active-directory-users-data-via-powershell/)**
- **[Intalling Chocolatey for Package Management](https://chocolatey.org/install)**
- **[What is Chocolatey](https://chocolatey.org/why-chocolatey)**
- **[What is Nuget](https://docs.microsoft.com/en-us/nuget/what-is-nuget)**
