import urllib.request
print("--------Starting Download--------")
url="http://s7ap1.scene7.com/is/image/tatamotors/CosmicGold-0-1?$PO-750-500-S$&fit=crop&fmt=avif-alpha"
#download file with urlretrieve
urllib.request.urlretrieve(url,"firstdream.png")
url="https://s7ap1.scene7.com/is/image/tatamotors/StardustAsh-0-1?$PO-750-500-S$&fit=crop&fmt=avif-alpha"
with urllib.request.urlopen(url) as response:
    print("Status: ",response.status)
    print("downloading the image")
    with open("seconddream.png","wb") as image:
        image.write(response.read())
        