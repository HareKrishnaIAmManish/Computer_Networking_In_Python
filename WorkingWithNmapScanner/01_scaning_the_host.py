import nmap
port_scan=nmap.PortScanner()
#results=port_scan.scan('49.50.109.66','80-85','-sV') #sV version detection
# results=port_scan.scan('49.50.109.66','443','-sV')
results=port_scan.scan('49.50.109.66','22','-sV')
print(results)
print("---------------------------")
print(port_scan.command_line())
