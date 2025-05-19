import optparse
from socket import *
from threading import *
def socketScan(host,port):
    try:
        socket_connect=socket(AF_INET,SOCK_STREAM)
        socket_connect.settimeout(5)
        result=socket_connect.connect((host,port))
        print(' [+] %d/tcp open' %port)
    except Exception as e:
        print('[-] %d/tcp closed' % port) 
        print('[-] Reason:%s' %str(e))
    finally:
        socket_connect.close()
def portScanning(host,ports):
    try:
        ip=gethostbyname(host) 
        print('[+] Scan Results for : '+ ip) 
    except:
        print("[-] cannot resolve '%s' unknown host" %host)
        return
    for port in ports:
        t=Thread(target=socketScan,args=(ip,int(port)))
        t.start()
def main():
    parser=optparse.OptionParser('fname.py '+ '-H <Host> -P <Port>')
    parser.add_option('-H', dest='host',type='string',help='specify_host')
    parser.add_option('-P', dest='port',type='string',help='specify ports seperated by comma')
    (options,args)=parser.parse_args()
    host=options.host
    ports=str(options.port).split(',')
    if (host==None) | (ports[0] == None):
        print(parser.usage)
        exit(0)
    portScanning(host,ports)
if __name__=='__main__':
    main()
            