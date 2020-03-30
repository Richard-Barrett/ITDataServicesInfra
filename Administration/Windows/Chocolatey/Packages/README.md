## Packages
This area is to track any and all changes made with the [Chocolatey Package Manager](https://chocolatey.org/) as a result, there are three area here that focus on Developer Builds, Local Builds, and Server Builds. 
Furthermore, there is an option here to help organize security for packages on the [Chocolatey Package Manager Website](https://chocolatey.org/docs/security) that checks for specific vulnerabilities for packages you may wish to install. 
The default scripts here will install all packages listed in the specific package file by default. 
If you wish to install a package one at a time you do the following to help you install packages one at a time:

**Get Help Instructions Similar to a Man Page**
- **`<choco --help`** or **`choco -h`**

**Install a Package Manually with Prompt to Install**
- **`choco install <package>`**

**Install a Package Manually without a Prompt to Install**
- **`choco install <package> -y`**

**NOTE: THE SCRIPTS IN THIS DIRECTORY INSTALL ALL PACKAGES RESPECTIVE TO THE FILE DEVELOPER, LOCAL, AND SERVER**

**References**
- **[Chocolatey Packages Available](https://chocolatey.org/packages)**
- **[Chocolatey Security](https://chocolatey.org/docs/security)**

## Install Packages
To install packages use the script that will help you provision your machine to what you want to use.
The machine you are provisoning may be a machine used by a devloper. 
Or, the machine you are provisioning may be used for your local and/or a server. 
Provision Accordingly, and use the proper script with a security and minimal perspective in mind. 
Also, if you do not want to install any of those packages you can make own **`Packages.txt`** file.
By default any **`.txt`** file is set to be ignored.
However, the script **`Choco_Install_Packages.ps1`** will account for the **`Packages.txt`** file. 

**To Install Developer Packages**
- **`./Choco_Developer_Pacakages.ps1`**

**To Install Local Packages**
- **`./Choco_Local_Pacakages.ps1`**

**To Install Personal Packages**
- **`./Choco_Personal_Pacakages.ps1`**

**To Install Sever Packages**
- **`./Choco_Server_Pacakages.ps1`**

## Important Directories 
There are 5 directories within this area. 
```bash
├───Custom
├───Developer
├───Local
├───Personal
└───Server
```

These five directories allow you to recursively install packages and iterate over a **`Packages.txt`** file within each corresponding directory. You can look at the following directory links to get a better idea of what would be installed. 

- **[Custom](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Administration/Windows/Chocolatey/Packages/Custom)**
- **[Developer](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Administration/Windows/Chocolatey/Packages/Developer)**
- **[Local](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Administration/Windows/Chocolatey/Packages/Local)**
- **[Personal](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Administration/Windows/Chocolatey/Packages/Personal)**
- **[Server](https://github.com/Richard-Barrett/ITDataServicesInfra/tree/master/Administration/Windows/Chocolatey/Packages/Server)**

Each directory is named accordingly and you should only install what you want and need. 
I have designed these directories as templates with a particular group in mind that would need specific stuff installed on their machines. Furthermore the **`Custom`** directory allows you to make your own **`Custom_Packages.txt`** that will be completely ignored by git, so any changes you make won't impact commits or pulls. 

## How Are The Packages Installed with The Included Scripts
The packages are installed via a Powershell Script within the Directory:

- **`Choco_<DirectoryName>_Packages_Install.ps1`**

This allows users to iterate over a **`Packages.txt`** file with the following procedure that instantiates a forloop to install via the **`choco instal <package> -y`** command. The scripts contain the following to iterate over package names. 

- **`<package output command> | Foreach-Object { choc install $_ -y }`**
