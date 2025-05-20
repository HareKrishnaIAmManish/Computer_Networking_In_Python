import json
import urllib.request
# response=urllib.request.urlopen('https://www.google.com/',timeout=30)
response=urllib.request.urlopen('https://httpbin.org/get',timeout=30)
# print(response)
data=response.read()
print(data)
json_response=json.loads(data)
print(json_response)

