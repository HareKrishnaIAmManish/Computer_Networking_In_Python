import socket
try:
    result=socket.gethostbyaddr("8.8.8.8")
    print(result)
    print("the hostname is ",result[0])
    print("ip addresses are")
    for item in result[2]:
        print(" "+item)
except socket.error as e:
    print("error for resolving ip addresses:",e)        