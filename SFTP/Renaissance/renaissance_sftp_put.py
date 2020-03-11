import os
import paramiko
import sys

# set up logging
from paramiko.py3compat import input

paramiko.util.log_to_file('clever_ftp_log')

make_ssh_connexion = paramiko.SSHClient()
make_ssh_connexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = "s<>"
user_name = "<>"
pass_word = "<>"
port_num = "<>"
# print("Connecting...")
# print(host)
# print(key_file)
make_ssh_connexion.connect(hostname = host, username = user_name, password = pass_word)

# print("connected!")
sftp = make_ssh_connexion.open_sftp()

sftp.put('OneRoster/academicSessions.csv','academicSessions.csv')
sftp.put('OneRoster/classes.csv','classes.csv')
sftp.put('OneRoster/courses.csv','courses.csv')
sftp.put('OneRoster/demographics.csv','demographics.csv')
sftp.put('OneRoster/enrollments.csv','enrollments.csv')
sftp.put('OneRoster/orgs.csv','orgs.csv')
sftp.put('OneRoster/users.csv','users.csv')


# source='/admin.csv'
# destination='/admin.csv'

make_ssh_connexion.close()
