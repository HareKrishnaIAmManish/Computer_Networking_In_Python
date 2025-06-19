import nmap
import argparse
def callBackFTP(host,result):
    try:
        script=result['scan'][host]['tcp'][21]['script']
        print("Command line"+result['nmap']['command_line'])
        for key,value in script.items():
            print('Script {0} --> {1}'.format(key,value))
    except KeyError:
        pass
class NmapScannerAsyncFTP:
    def __init__(self):
        self.portScanner=nmap.PortScanner()
        self.portScannerAsync=nmap.PortScannerAsync()            
    def scanning(self):
        while self.portScannerAsync.still_scanning():
            print("Scanning >>>")
            self.portScannerAsync.wait(10)
    def nmapScanAsync(self,hostname,port):
        try:
            print('checking port ' + port +'.......') 
            self.portScanner.scan(hostname,port)
            self.state=self.portScanner[hostname]['tcp'][int(port)]['state']
            print("  [+]   "+hostname + " tcp/" +port +" "+self.state)
            #checking ftp service
            if (port=='21') and self.portScanner[hostname]['tcp'][int(port)]['state']=='open':
                print('checking ftp port with nmap scripts ......')
                print('Checking ftp-anon.nse.......')
                self.portScannerAsync.scan(hostname,arguments="-A -sV -p21 --script ftp-anon.nse",callback=callBackFTP)
                self.scanning()   
                print('Checking ftp-bounce.nse....')
                self.portScannerAsync.scan(hostname,arguments="-A -sV -p21 --script ftp-bounce.nse",callback=callBackFTP)
                self.scanning()
                print('checking ftp-libopie.nse .......')
                self.portScannerAsync.scan(hostname,arguments="-A -sV -p21 --script ftp-libopie.nse",callback=callBackFTP)
                self.scanning()
                print('checking ftp-proftpd-backdoor.nse.......')
                self.portScannerAsync.scan(hostname,arguments="-A -sV -p21 --script ftp-proftpd-backdoor.nse",callback=callBackFTP)
                self.scanning()
                print('checking ftp-vsftpd-backdoor.nse .......')
                self.portScannerAsync.scan(hostname,arguments="-A -sV -p21 --script ftp-vsftpd-backdoor.nse",callback=callBackFTP)
                self.scanning()
        except Exception as e:
            print("error to connect with "+ hostname + " for port scanning",str(e))        
if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Asynchronous Nmap scanner') 
    parser.add_argument("--host",dest="host",help="target IP/domain",required=True)
    parsed_args=parser.parse_args()
    host=parsed_args.host
    scanner=NmapScannerAsyncFTP()
    scanner.nmapScanAsync(host,'21')
        

