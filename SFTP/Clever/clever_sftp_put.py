import os
import paramiko
import sys

# set up logging
from paramiko.py3compat import input

paramiko.util.log_to_file('clever_ftp_log')

make_ssh_connexion = paramiko.SSHClient()
make_ssh_connexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = "<host>"
user_name = "<username>"
pass_word = "<password>"
port_num = "<port>?"
# print("Connecting...")
# print(host)
# print(key_file)
make_ssh_connexion.connect(hostname = host, username = user_name, password = pass_word)

# print("connected!")
sftp = make_ssh_connexion.open_sftp()

sftp.put('admins.csv','admins.csv')
sftp.put('teachers.csv','teachers.csv')
sftp.put('students.csv','students.csv')
sftp.put('enrollments.csv','enrollments.csv')
sftp.put('schools.csv','schools.csv')
sftp.put('sections.csv','sections.csv')

# source='/admin.csv'
# destination='/admin.csv'

make_ssh_connexion.close()

# print("Closed and quitting. Dan is the most awesome!")
