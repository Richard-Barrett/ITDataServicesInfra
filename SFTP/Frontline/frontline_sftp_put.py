import paramiko
import os

# os.remove('peimsexp.csv')

# set up logging
from paramiko.py3compat import input

paramiko.util.log_to_file('peims_ftp_log')

make_ssh_connexion = paramiko.SSHClient()
make_ssh_connexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = "<host>"
user_name = "<username>"
pass_word = "<passowrd>"
port_num = "<port>"
# print("Connecting...")
# print(host)
# print(key_file)
make_ssh_connexion.connect(hostname = host, username = user_name, password = pass_word)

# print("connected!")
sftp = make_ssh_connexion.open_sftp()

if os.path.exists('peimsexp.csv'):
    os.remove('peimsexp.csv')
sftp.get('peimsexp.csv', 'peimsexp.csv')
sftp.put('peimsexp.csv', 'peimsexp.csv')

make_ssh_connexion.close()
