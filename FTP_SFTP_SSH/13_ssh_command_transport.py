import paramiko
import getpass
import paramiko.transport
def run_ssh_command(hostname,user,passwd,command):
    transport=paramiko.Transport(hostname)
    try:
        transport.start_client()
    except Exception as e:
        print(e)
    try:
        transport.auth_password(username=user,password=passwd)
    except Exception as e:
        print(e)
    if transport.is_authenticated():
        print(transport.getpeername())
        channel=transport.open_session()
        channel.exec_command(command)
        response=channel.recv(1024)
        print('Command %r(%r)---->%s'%(command,user,response)) 
if __name__=="__main__":
    hostname=""
    port=22
    username=""
    password=""
    command="ls"
    run_ssh_command(hostname,username,password,command)
