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
cnt1=protocols.count("ssh")
print(cnt1)
protocols.append("ssh")
cnt2=protocols.count("ssh")
print(cnt2)
print(protocols)
protocols.insert(0,"Mandy")
print(protocols)
print(len(protocols))
protocols.remove("Mandy")
print(protocols)
protocols.reverse()
print(protocols)
print(protocols.pop())
print(protocols)
print(len(protocols))
print(protocols)
protocols[9]="mandy"
print(protocols)
protocols.insert(4,"bye") #(index,val)
print(protocols)
print(protocols[1:4])
print(protocols[1:4:1])
print(protocols)
print(protocols[::2])
print(protocols[::-2])
print(protocols)
print(protocols[::-3])

