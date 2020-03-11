import os
import paramiko
import sys

# set up logging
from paramiko.py3compat import input

paramiko.util.log_to_file('clever_ftp_log')

make_ssh_connexion = paramiko.SSHClient()
make_ssh_connexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host= '<hostname>'
user_name="<username>"
pass_word="<password>"
port_num="<port>"
# print("Connecting...")
# print(host)
# print(key_file)
make_ssh_connexion.connect(hostname = host, username = user_name, password = pass_word)

# print("connected!")
sftp = make_ssh_connexion.open_sftp()

sftp.put('AESOP_Time_Off_Balances.csv', 'AESOP_Time_Off_Balances.csv')

make_ssh_connexion.close()

# print("Closed and quitting. Copied from OneRoster\Renaissance DRC Python Script, yes DRC is Awsome!")

