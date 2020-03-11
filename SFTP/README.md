# SFTP
SFTP is a common protocol used to send vendors information. 
As a result, I have included some common scripts that might help school districts with their overall code infrastructure. 
The main thing is security. As such I am including several templates that work with Bash, Powershell, and Python to help users send files securely to and from SFTP locations external and internal to their own inrastructure. 

How does the SFTP Directory work?
The SFTP Directory works by allowing you to store a script and/or any relevant files without having them exposed to the Repository and/or the internet, while keeping track of your code. It also allows you to store credentials within each working directory you need for SFTP. For Example, in the following:
```
PS C:\Users\richard.barrett\Git\ITDataServicesInfra\SFTP> tree
Folder PATH listing for volume OS
Volume serial number is 1E07-4DEE
C:.
├───Aesop
├───Cardonex
├───Clever
├───Frontline
├───Renaissance
├───SchooLinks
├───Scripts
├───Skyward
└───TalentEd
```
In each directory you can store a **files.json** or **files.txt**, a **secrets.json** or **secrets.txt**, and any relvant files **.csv**, **.xlsx**, **.pdf** within each directory. It also makes it easy for you to replace SFTP credentials given to you by third party vendors that you use for operational programs throughout your organization. 

## Powershell
A common Powershell Template to help with sending files to SFTP locations.
The main key is that you call two files here **secrets.txt** and **files.txt** within the code to pass off files and/or passwords without exposing file locations and credentials over Internet Traffic and/or as an exposed process often due to hardcoded information within code. Another method is calling it using GnuPG Encrypted files using the Get-Content command from **secrets.gpg** and a **files.gpg** file. Also the scripts are dependent on WinSCP. 

The **secrets.txt** file should look similar to this template:
```powershell
Protocol = [WinSCP.Protocol]::Sftp
HostName = "<hostname>"
UserName = "<username>"
Password = "<password>"
SshHostKeyFingerprint = "ssh-rsa <encryption_type> <fingerprint_string>"
```

The **files.txt** file should look similar to this template:
```powershell
$localPath = '<absolute_path>',
$remotePath = '<absolute_path>'
```

The commands that pull out the information and pass it into the script are `Get-Content <file> | Select-String "<parsing_string>"`

**Powershell SFTP Template**
```powershell
param (
    Get-Content .\files.txt | Select-String "localPath"
    Get-Content .\files.txt | Select-String "remotePath"
)
 
try
{
    # Load WinSCP .NET assembly
    Add-Type -Path "C:\Program Files (x86)\WinSCP\WinSCPnet.dll"
 
    # Setup session options
    $sessionOptions = New-Object WinSCP.SessionOptions -Property @{
        Get-Content .\secrets.txt | select-string "Protocol"
        Get-Content .\secrets.txt | select-string "HostName"
        Get-Content .\secrets.txt | select-string "UserName"
        Get-Content .\secrets.txt | select-string "Password"
        Get-Content .\secrets.txt | select-string "SshHostKeyFingerprint"
    }
 
    $session = New-Object WinSCP.Session
 
    try
    {
        # Connect
        $session.Open($sessionOptions)
 
        # Upload files
        $transferOptions = New-Object WinSCP.TransferOptions
        $transferOptions.TransferMode = [WinSCP.TransferMode]::Binary
 
        $transferResult =
            $session.GetFiles($remotePath, $localPath, $False, $transferOptions)
 
        # Throw on any error
        $transferResult.Check()
 
        # Print results
        foreach ($transfer in $transferResult.Transfers)
        {
            Write-Host "Download of $($transfer.FileName) succeeded"
        }
    }
    finally
    {
        # Disconnect, clean up
        $session.Dispose()
    }
 
    exit 0
}
catch
{
    Write-Host "Error: $($_.Exception.Message)"
    exit 1
}
```

## Python
A common Python template to help with sending files to SFTP locations. 
The main key is that you call two files here **secrets.json** and **files.json** within the code to pass off files and/or passwords without exposing file locations and credentials over Internet Traffic and/or as an exposed process often due to hardcoded information within code. 

The **secrets.json** file should look similar to this template:
```json
{
  "sftp_credential": {
    "host": "<hostname>",
    "username": "<username>",
    "password": "password",
    "port_num": "<port>",
    "key_file": "<direct_path>"
  }
}
```
The **files.json** should look similar to the following:
```json
{
  "get_files": {
    "file_1": "<absolute_path>",
    "file_2": "<absolute_path>",
    "file_3": "<absolute_path>",
    "file_4": "<absolute_path>",
    "file_5": "<absolute_path>"
  },
  "put_files": {
    "file_1": "<absolute_path>",
    "file_2": "<absolute_path>",
    "file_3": "<absolute_path>",
    "file_4": "<absolute_path>",
    "file_5": "<absolute_path>"
  }
}
```
The overall goal is to not expose file locations or system paths within the process. 
The other part is to call the password from either an encrypted or non-encrypted file, instead of hardcoding it to the script. 

**Python SFTP Template**
```python
import os
import paramiko
import sys
import json
with open('secrets.json','r') as f:
      config = json.load(f)
    
# set up logging
from paramiko.py3compat import input

paramiko.util.log_to_file('clever_ftp_log')

make_ssh_connexion = paramiko.SSHClient()
make_ssh_connexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# JSON File Should Contain the Folling Information
# File should be named as secrets.json
# Category should be sftp_credential

# Nested Objects
# host= '<hostname>'
# username="<username>"
# password="<password>"
# port_num="<port>"
# key_file="<direct_path>"

print("Connecting...")
print((config['sftp_crentential']['host']))
print((config['sftp_crentential']['key_file']))

make_ssh_connexion.connect(hostname = (config['sftp_crentential']['host']), 
                           username = (config['sftp_crentential']['username']), 
                           password = (config['sftp_crentential']['password']))

# print("connected!")
sftp = make_ssh_connexion.open_sftp()

with open('files.json','r') as f:
      file = json.load(f)
 
# JSON File Should Contain the Folling Information
# File Should be named files.json
# File should be referenced as Files:
# After Files: File_1 should be nested as "file_1":"/Directory/Path/Filename"
# You can Change the files.json File by enumerating with file_# as an index.

sftp.put((file['files']['file_1']), 
         (file['files']['file_2']),
         (file['files']['file_3']),
        )

make_ssh_connexion.close()
print("Process Complete!")
```

