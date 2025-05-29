import paramiko
import subprocess
ssh_client=paramiko.SSHClient()
hostname=''
port=22
username=''
password=''
ssh_client.connect(hostname,port,username,password)
for line in stdout.readlines():
    print(line.strip())
ssh_client.close()
