import urllib.request
import urllib.parse
data_dictionary={"id":"0123456789"}
print(data_dictionary)
data=urllib.parse.urlencode(data_dictionary)
print(data)
data=data.encode('ascii')
print(data)
with urllib.request.urlopen("http://httpbin.org/post",data) as response:
    print(response.read().decode('utf-8'))
    
