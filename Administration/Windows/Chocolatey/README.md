## Packages
Packages are Chocolatey Packages that you can install via the Chocolatey Package Manager. 
As a result, you can find a list of all of the packages available via the following link:

- **[Chocolatey Packages](https://chocolatey.org/packages)**

## References
Some people may be unfamilliar with Chocolatey. 
As a result, I have included the following link to helo you better understand how to use choclatey within Powershell. 

- **[Chocolatey Commands Cheatsheet](https://chocolatey.org/docs/commandslist)**

## Security 
Chocolatey by default does not work with Git in terms of Checking Auomtated Security. 
As a result, there are some python scripts that will check all packages installed and within the repsosiotry. 
This script will notify you and automate create a pull request within the repostiory. 
Furthermore, it will notify the Developer, Local, and Server users when a vulernability is present. 
Also there is a script that will allow you to see the vulnerabilities preset on a Windows Machine via Powershell. 
This is similar to the [Python Safety Check](https://pyup.io/safety/).
