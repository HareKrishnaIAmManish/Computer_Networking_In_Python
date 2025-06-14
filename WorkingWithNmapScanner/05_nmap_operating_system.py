import nmap,sys
command="OS_detection.py <hostname/IP address>"
if len(sys.argv)==1:
    print(command)
    sys.exit()
host=sys.argv[1]
portscanner=nmap.PortScanner()
open_ports_dict=portscanner.scan(host,arguments="-O -v")
if open_ports_dict is not None:
    open_ports_dict=open_ports_dict.get("scan").get(host).get("tcp")
    print("Open Ports description")
    port_list=open_ports_dict.keys()
    for port in port_list:
        print(port,"----\t--->",open_ports_dict.get(port)['name'])
    print("\n-----------------------OS details----------------\n")
    #print(portScanner[host])
    print("Details about the scanned hosts are: \t",portscanner[host]['osmatch'][0]['osclass'][0]['cpe'])
    print("Operating system family is : \t\t",portscanner[host]['osmatch'][0]['osclass'][0]['osfamily'])
    print("Type of OS is: \t\t\t\t",portscanner[host]['osmatch'][0]['osclass'][0]['type'])
    print("Generation of Operating System: \t",portscanner[host]['osmatch'][0]['osclass'][0]['osgen'])
    print("Operating system vendor is:  \t\t",portscanner[host]['osmatch'][0]['osclass'][0]['vendor'])
    print("Accuracy of detection is:\t\t",portscanner[host]['osmatch'][0]['osclass'][0]['accuracy'])
        
