with open("hello.txt","r") as f:
    contet=f.read()
    print(contet)
with open("hello.txt","rb") as f:
    contet=f.read()
    print(contet)
