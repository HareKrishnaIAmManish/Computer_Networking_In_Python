import nmap
# print(dir(nmap))
port_scan=nmap.PortScanner()
# print(dir(port_scan))
print(help(port_scan.scan))
