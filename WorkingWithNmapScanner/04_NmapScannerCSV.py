import optparse
import nmap
import csv
class NmapScannerCSV:
    def __init__(self):
        self.portScanner=nmap.PortScanner()
    def nmapScanCSV(self,host,ports):
        try:
            print("Checking Ports: "+str(ports) + " ....................")
            self.portScanner.scan(host,arguments='-n -p'+ports)
            print(" [*] Executing command: %s"%self.portScanner.command_line())
            print("-----------------------------------------")
            print(self.portScanner.csv())
            print("-----------------------------------------")
            print("summary for host",host)
            with open('csv_file.csv',mode='w') as csv_file:
                csv_writer=csv.writer(csv_file,delimiter=',') #delimeter is that , will be used to seperate
                csv_writer.writerow(['Host','Protocol','Port','State'])
                for x in self.portScanner.csv().split("\n")[1:-1]:
                    splited_line=x.split(";")
                    host=splited_line[0]
                    protocol=splited_line[5]
                    port=splited_line[4]
                    state=splited_line[6]
                    print("Protocol:",protocol,"Port:",port,"State:",state)
                    csv_writer.writerow([host,protocol,port,state])
        except Exception as e:
            print("Error to connect with "+host+" for port scanning",e)
def main():
    parser=optparse.OptionParser("usage%prog "+"--host <target host> --ports <target port>")
    parser.add_option('--host',dest='host',type='string',help="specify the host")
    parser.add_option('--ports',dest='ports',type='string',help='please specify the target ports seperated by ,')
    (options,arguments)=parser.parse_args()
    if(options.host==None)| (options.ports==None):
        print("[-] You must specify the both ip addresses and ports")
        exit(0)
    host=options.host
    ports=options.ports
    NmapScannerCSV().nmapScanCSV(host,ports)
if __name__=='__main__':
    main()
