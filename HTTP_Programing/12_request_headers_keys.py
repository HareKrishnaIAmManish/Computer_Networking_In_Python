import requests
if __name__=='__main__':
    domain=input("enter the host name https://")
    response=requests.get("https://"+domain)
    for header in response.headers.keys():
        print("--------------header is--------------------------")
        print(header)
        print("response.header is ")
        print(response.headers[header])
        print(header  + ":" + response.headers[header])
