with open("baby.txt","r+b") as f:
    f.write(b"wo hoo waah ou")
    f.seek(0)
    print(f.read())
    