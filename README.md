## Welcome to ITDataServicesInfra
![Image](https://triking-creative.s3.amazonaws.com/Logos/ITDataServicesInfra/ITDataServicesInfra.PNG)

You can access Documentation by navigating to the following URLS within the Repository Public Wiki:
- [Documentation](https://github.com/Richard-Barrett/ITDataServicesInfra/wiki)
- [Purpose](https://github.com/Richard-Barrett/ITDataServicesInfra/wiki/ITDataServicesInfra-Purpose)
- [Directories](https://github.com/Richard-Barrett/ITDataServicesInfra/wiki/Directories)

## Getting Started

To get started with using this repository you will need to first have Git Installed (Please See [Documentation](https://github.com/Richard-Barrett/ITDataServicesInfra/wiki) for further detailed on the Home Page in our repository wiki). Please ensure you have used the following steps to properly set up this repository. If you **FAIL TO FOLLOW THESE STEPS THE GIT REPOSITORY WILL NOT FUNCTION CORRECTLY!!!**
1. Please make a Git directory within the home directory for the service account that will be using this repository.
- **`mkdir Git`**
2. Change your Working Directory so that you see C:\Users\service_user\Git for Windows or /Users/service_user/Git for Linux and Mac
- **`cd Git`**
3. Clone the repository by using the following Git Clone command after folliing installation instructions within [Documentation](https://github.com/Richard-Barrett/ITDataServicesInfra/wiki)
- **`git clone https://github.com/Richard-Barrett/ITDataServicesInfra.git`**

For **Windows Users** please make sure that you make the directory **Git** and **`git clone`** the repository so your working directory looks the following:
1. Local Machine for Remote Pushing and Change Management
- **`C:\Users\richard.barrett\Git\ITDataServicesInfra\`**
2. For Serving and Storing the Repository on a Server/VM as the **Master Branch** for data interaction.
- **`C:\Git\ITDataServicesInfra\`**

For **Linux/Mac Users** please make sure that you make the directory **Git** and **`git clone`** the repository so your working directory looks the following:
1. Local Machine for Remote Pushing and Change Management
- **`/home/richard.barrett/Git/ITDataServicesInfra`**
2. For Serving and Storing the Repository on a Server/VM as the **Master Branch** Under the **Service_Account and/or Root User** for data interaction:
- **`/srv/Git/ITDataServicesInfra/`**

## Using Git 

You can add files to git within your terminal, while you are coding. 
As you can imagine it makes life a lot easier. You can use whatever in-line text editor you want to use: Vim, Nano, Vi, etc.

If you want to see that status of you branch:
- **`git status`**

If you want to pull down any changes to your local repo:
- **`git pull`**

If you want to see a log of all commits
- **`git log`**

If you want to show the details of a particular commit within git log:
- **`git show <commit_id>`**

To Make a change:
- **`vim test`**

Add All Changes for a Commit:
- **`git add -A`**

Commit All Changes Added:
- **`git commit -a`**

Make sure you put some note as to what the change is, otherwise there is no description and/or notes regarding what was changed.

Review and/or Push the Change:
- **`git review`** - Optional if you are using Gerrit, Gitlab, Bitbucket, etc. for code review from peers.
- **`git push`** - If you are the maintainer, you can push changes. 

## Working with Git

Git gives you the capability to see what changes were made, check the status, make branches to develop, checkout different branches, and look at what changes were added to specifc commits. 

## Understanding Git Security

Git has the ability to ignore certain files for commit. 
What this means is that certain files that have certain extensions defined within the **`.gitignore`** file will not be added into the repository. They do not exist within the repository. These files instead exist on the local machine. If they are defined within the **`.gitignore`** file, then they are never staged to be commited to the repository. Certain file extensions have been specifically ignored for this repository with security in mind. The following files are set to be ignored:

- **`.csv`** - Comma Separated Value Files
- **`.doc`** - Word Procesing Document
- **`.gpg`** - GNU Privacy Guard **(GnuPG)** File 
- **`.json`** - JavaScript Object Notation File
- **`.pdf`** - Portable Document Format Files
- **`.rpt`** - Crystal Report Files
- **`.txt`** - Text Files
- **`.xlsm`** - Microsoft Exel File Format
- **`.xlsx`** - Microsoft Exel File Format
- **`.xltm`** - Microsoft Exel File Format
- **`.xltx`** - Microsoft Exel File Format

Other file extensions will be added overtime and will be defined within the **`.gitignore`** file. 
Microsoft Office files for Documents and/or Spreadsheets containing sensitive information are set to be ignored by default. 
Text Files and JSON files are also set to be ignored for security reasons if you are using flatfiles on your local to passoff credentials. Furthermore, if you are implementing GPG Encryption for files containing secret and secure information, all such files are also set to be ignored on the system. In **Git** you should never store and/or commit information that is secure and needs to be hidden. This repository also assumes that you understand how to work with **Git** and accepts no liability for any security breaches incurred. 

## Understanding the `.gitignore` File

## Web Scraping
Web scraping is a mean in which you can automate a lot of your data export and imports. What this means is that you can use the repository in the following manner to help aid you in this process. Please see the following image to understand how Web Scraping works in terms of the overall process flow. 

![Image](https://www.lucidchart.com/publicSegments/view/55833c2f-f932-4b14-8d16-9748c609e03e/image.jpeg)

## Understanding The Repository 
The [Purpose](https://github.com/Richard-Barrett/ITDataServicesInfra/wiki/ITDataServicesInfra-Purpose) will help you centralize a lot of your data interactions for exporting and importing data from third party websites and interacting with your local database for Imports. 
The repository has [Directories](https://github.com/Richard-Barrett/ITDataServicesInfra/wiki/Directories), each Directory has a README.txt on how to use the directory. Furthermore, the [Directories](https://github.com/Richard-Barrett/ITDataServicesInfra/wiki/Directories) page on our Wiki will give you a thourough understanding in how each directory is used and how you can use it to fit your own Entity's/Organization's needs.

**Common Workflow**
![Image](https://www.lucidchart.com/publicSegments/view/91a39f7e-e9be-4c20-b819-4d2974bdc93a/image.jpeg)

## Virtualization Set Up
If you want to use this repository in a virtualized environment, you can also look at the **Virtualization** directory within the repository. In this directory you can virtualize a lot of the processes as well as spin up infrastructure quick and easy. Please refer to your local policies within your entity and/or organization before continuing down this path. Basically you can containerize, or you can spin up a cloud on-premises option.

## Installing Ruby

![Image](https://chocolatey.org/content/packageimages/ruby.2.7.0.1.svg)

Ruby is a great dev tool. If you want to install it for your Virtual Machine, Local, or Cloud Based Instance. Please follow the following steps and guidelines to install Ruby. 
1. [Linux Ubuntu](https://www.thoughtco.com/instal-ruby-on-linux-2908370)
- **`sudo apt-get install ruby-full`**
2. [Windows 10 with Chocolatey](https://chocolatey.org/docs/installation)
- **`choco install ruby`**
3. [MacOS with Brew](https://docs.brew.sh/Installation)
- **`brew install ruby`**

## Installing Python

![Image](https://www.python.org/static/img/python-logo@2x.png)

Python is the primary mode here in terms of interacting with all of the components. You definitely need to download it, furthermore if you are starting with Python you might want to know that 2020 is the deprecation timeframe for Python2.7 so we are using Python3.6 here. 
1. [Linux Ubuntu](https://docs.python-guide.org/starting/install3/linux/)
- **`sudo apt-get update`**
- **`sudo apt-get install python3.6`**
2. [Windows 10 with Chocolatey](https://chocolatey.org/packages/python/3.8.1.20200110#description)
- **`choco install python`**
3. [MacOS with Brew](https://docs.python-guide.org/starting/install3/osx/)
- **`brew install python`**

## Installing & Using Brew

![Image](https://brew.sh/assets/img/homebrew-256x256.png)

If you want a better experience with MacOS you can download the package manager for MacOS by following the link below and using the instructions to help you install and initialize Homebrew.
1. [Brew The MacOS Package Manager](https://brew.sh/)
2. [Brew Tutorials](https://www.datacamp.com/community/tutorials/homebrew-install-use)
3. Following Data Camp's steps you can download and install Homebrew in the following manner by opening a terminal session and copying an pasting in the following information. 
- **`xcode-select -p`**
- **`xcode-select --install`**
- **`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`**

## Installing & Using Chocolatey

![Image](https://chocolatey.org/content/images/logo_square.svg)

If you want to use a package manager for **Windows 10** and **Windows Server** it is recommended that you use Chocolatey. You can install Chocolatey by making sure you fullfill the following requriements:
- **Windows 7+ / Windows Server 2003+**
- **PowerShell v2+ (Not PowerShell Core yet though)**
- **.NET Framework 4+ (the installation will attempt to install .NET 4.0 if you do not have it installed)**
To get the package manager installed on your local Windows Machine or Server, open Powershell by Clicking Run as Admin and enter the following on the prompt:
- **`Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`**
- **A.** [Installing Chocolatey](https://chocolatey.org/docs/installation)
- **B.** [Chocolatey Documentation](https://chocolatey.org/docs/)
- **C.** [Chocolatey Packages](https://chocolatey.org/packages)


