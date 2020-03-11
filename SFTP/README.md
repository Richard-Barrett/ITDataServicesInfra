# SFTP
SFTP is a common protocol used to send vendors information. 
As a result, I have included some common scripts that might help school districts with their overall code infrastructure. 
The main thing is security. As such I am including several templates that work with Bash, Powershell, and Python to help users send files securely to and from SFTP locations external and internal to their own inrastructure. 

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
    "port_num": "<port>"
    "key_file": "<direct_path>"
  }
}
```
The **files.json** should look similar to the following:
```json
{
  "files": {
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

