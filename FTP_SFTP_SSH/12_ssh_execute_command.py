import getpass
import paramiko
HOSTNAME=''
PORT=22
def run_ssh_cmd(username,password,command,hostname=HOSTNAME,port=PORT):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()
    ssh_client.connect(hostname,port,username,password)
    stdin,stdout,stderr=ssh_client.exec_command(command)
    #print(stdout.read())
    stdin.close()
    for line in stdout.read().splitlines():
        print(line.decode())
if __name__=='__main__':
    #hostname=input("Enter the target hostname :")
    hostname=''
    port=22
    #port=input("Enter the target port: ")
    #username=input("Enter Username: ")
    #username="laptop-j0snp13t\manis"
    #password=getpass.getpass(prompt="Enter the password: ")
    #password="Lap123"
    username=""
    password=""
    #command=input("Enter command: ")
    #command="python --version"
    command=command="cd Desktop/hacked && echo 'hello umma' > myfile.txt"
    run_ssh_cmd(username,password,command)   