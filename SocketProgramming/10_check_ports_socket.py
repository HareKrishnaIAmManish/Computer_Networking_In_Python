import socket
import sys
def checkPortsSocket(ip,portlist):
    try:
        for port in portlist:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result=sock.connect_ex((ip,port))
            if result ==0:
                print("Port {}: \t Open".format(port))
            else:
                print("Port {}: \t Closed".format(port))
            sock.close()
    except socket.error as e:
        print(str(e))        
        print("connection error")
        sys.exit()    
# checkPortsSocket('localhost',[21,22,80,8080,443])    
checkPortsSocket('49.50.109.66',[21,22,80,8080,443])        