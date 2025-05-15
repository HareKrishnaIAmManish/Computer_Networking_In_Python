with open("bye.txt","w") as f:
    f.write("bye  love you")
#r+ ->reading and writing the file must exist,it overwrites from the start unless you move the cursor
with open("bye.txt","r+") as f:
    content=f.read()
    print(content)
    f.seek(0) 
    f.write("umma")
    f.seek(0)
    content=f.read()
    print(content)
    