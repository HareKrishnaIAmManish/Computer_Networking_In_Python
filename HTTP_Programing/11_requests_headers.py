import requests,json
domain=input("enter the host name https://")
response=requests.get("https://"+domain)
print(response.json)
print("response status code:",str(response.status_code))
print("Headers response: ")
for header,value in response.headers.items():
    print(header,'--->',value)
print('--------------Headers request---------------')
for header,value in response.request.headers.items():
    print(header,'--->',value)
    