import requests
import os
shodan_api_key=''
ip='49.50.109.66'
def shodanInfo(ip):
    try:
        result=requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={shodan_api_key}&minify=True").json()
    except Exception as e:
        result={"error":"Information not available"} 
    return result 
print(shodanInfo(ip))
  