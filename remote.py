import paramiko
hostname = 'google.com'
usernname = 'lilian akinyi'
password = 'Kendie456!.'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=usernname, password=password)

stdin, stdout, stderr = ssh.exec_command('uptime')
print(stdout.read().decode())
ssh.close()
