import requests
respo=requests.get('http://www.python.org')
print(respo)
#print(respo.content)
print(respo.status_code)
