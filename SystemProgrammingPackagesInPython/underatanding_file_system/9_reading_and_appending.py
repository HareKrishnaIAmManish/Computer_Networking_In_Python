#File is opened for appending and reading.
#File is created if it doesn’t exist.
#All writes go to the end, regardless of seek()
with open("loveyou.txt","a+") as f:
    f.write("hyy")
    f.seek(0)
    f.write("\n umma")
    f.seek(0)
    print(f.read())
    