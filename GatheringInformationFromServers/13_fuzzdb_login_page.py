import requests
logins=[]
with open('Logins.txt','r') as filehandle:
    for line in filehandle:
        login=line[:-1]
        logins.append(login)
# domain="http://testphp.vulnweb.com/"        
#domain="https://www.iitism.ac.in/"
domain="https://pre-registration.iitism.ac.in"      
for login in logins:
    print("Checking..... "+domain+login)
    try:
     response=requests.get(domain+login)
     if response.status_code==200:
        print("-----------------------------------------")
        print("login resource detected: ",login)
        print("-----------------------------------------")
    except Exception as e:
           print("unable to scan this url",domain+login)
