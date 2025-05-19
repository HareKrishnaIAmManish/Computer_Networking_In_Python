import socket
import sys
from datetime import datetime
import errno
remoteServer=input("enter a remote server to scan: ")
remoteServerIP=socket.gethostbyname(remoteServer)
print("Please enter the range of ports you would like to scan on the machine")
startPort=input("enter the start port")
endPort=input("enter a end port :")
print("Please wait, scanning remote host", remoteServerIP)
time_init=datetime.now()
try:
    for port in range(int(startPort),int(endPort)):
        print("Checking port {}...".format(port))
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        result=sock.connect_ex((remoteServerIP,port))
        if result==0:
            print("port {}:    Open".format(port))
        else:
            print("port {}:    Closed".format(port))
            print("Reason:",errno.errorcode[result])
        sock.close()
except socket.error:
    print("couldnt connect to server")
    sys.exit()
time_finish=datetime.now()
totaltime=time_finish-time_init
print('port scanning completed in ',totaltime)
                
                