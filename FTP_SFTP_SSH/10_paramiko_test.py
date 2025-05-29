import paramiko
import socket
# put data about your ssh server
host='localhost'
usernane=''
password=''
try:
    ssh_client=paramiko.SSHClient()
    #the following shows the debug info
    paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG) # enables detailed logs for debugging and diagnosing issues.
    #the following lines add the server key automatically to the host file
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    response=ssh_client.connect(host,port=22,username=usernane,password=password)
    print('connected with host on port 22')
    print("the response is below")
    print(response)
    transport=ssh_client.get_transport()#transport object,paramiko.Transport object, low level transport object ,this object will handle the SSH protocol low levelly including encryption key exchange and authentication
    security_options=transport.get_security_options() #security options object to view the cryptographic settings
    print(security_options.kex) #kex ->key exchange
    print(security_options.ciphers) #symmetric encryption algorithms (ciphers)
except paramiko.BadAuthenticationType as e1:
    print("Bad authentication exception  ",e1)
except paramiko.SSHException as e2:
    print("SSHException :",e2) 
except socket.error as e3:
    print("Socket error: ",e3)
finally:
    print("closing connection")
    ssh_client.close()
    print("closed")
               





    
