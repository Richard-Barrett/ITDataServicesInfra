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

# Examples for files.json usecase 
# sftp.put('OneRoster/academicSessions.csv','academicSessions.csv')
# sftp.put('OneRoster/classes.csv','classes.csv')
# sftp.put('OneRoster/courses.csv','courses.csv')
# sftp.put('OneRoster/demographics.csv','demographics.csv')
# sftp.put('OneRoster/enrollments.csv','enrollments.csv')
# sftp.put('OneRoster/orgs.csv','orgs.csv')
# sftp.put('OneRoster/users.csv','users.csv')


# source='/admin.csv'
# destination='/admin.csv'
sftp.put((file['put_files']['file_1']), 
         (file['put_files']['file_2']),
         (file['put_files']['file_3']),
        )

make_ssh_connexion.close()
print("Process Complete!")
