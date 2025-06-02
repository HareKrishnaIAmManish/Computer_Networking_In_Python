import nmap
portScannerAsync=nmap.PortScannerAsync()
def callback_result(host,scan_result):
    print("-----This is callback-------")
    print(host,scan_result)
    print("-------call back ends-------")
portScannerAsync.scan(hosts='49.50.109.66',arguments='-p 21',callback=callback_result)
portScannerAsync.scan(hosts='49.50.109.66',arguments='-p 22',callback=callback_result)
portScannerAsync.scan(hosts='49.50.109.66',arguments='-p 23',callback=callback_result)
portScannerAsync.scan(hosts='49.50.109.66',arguments='-p 80',callback=callback_result)
while portScannerAsync.still_scanning():
    print("Scanning >>>")
    portScannerAsync.wait(5)
