protocols=[]
protocols.append("ssh")
protocols.append("ssh")
protocols.append("ftp")
protocols.append("smtp")
protocols.append("http")
protocols.append("")
protocols.append("5")
protocols.append(5)
protocols.append("9999299595")
protocols.append("5")
protocols.append("kali")
for i in range (1,4):
    if(protocols[i]=="kali"):
        print("kali found at ",i)
    else:
        print("kali not found at index ",i)
found=False
for i in range (len(protocols)):
    if(protocols[i]=="kali"):
        print("found at index ",i)
        found=True
        break
if not found:
    print("not there bye bye")

