import shodan
import requests
shodan_api_key=''
api=shodan.Shodan(shodan_api_key)
domain='www.iitism.ac.in' 
dnsResolve = f"https://api.shodan.io/dns/resolve?hostnames={domain}&key={shodan_api_key}"
try:
    resolved=requests.get(dnsResolve)
    hostIP=resolved.json()[domain]
    host=api.host(hostIP)
    print(type(host))
    print("IP: %s" %host['ip_str'])
    print("Organization: %s" % host.get('org','n/a'))
    print("Operating System: %s" % host.get('os','n/a'))
    for item in host['data']:
        print("Port: %s " %item['port'])
        print("Banner: %s" %item['data'])
except shodan.APIError as exception:
    print('Error: %s'%exception)
    
        
