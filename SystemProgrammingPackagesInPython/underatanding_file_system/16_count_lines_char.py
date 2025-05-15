try:
    countlines=countchars=0
    f=open("newfile.txt","r")
    lines=f.readlines()
    print(lines)
    for line in lines:
        print(line)
        countlines+=1
        for char in line:
            print(char)
            countchars+=1
    f.close()
    print("“Characters in file:”", countchars)
    print("“Lines in file:”", countlines)
except Exception as e:
    print("error is",e)
