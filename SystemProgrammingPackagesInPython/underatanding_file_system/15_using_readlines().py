with open("baby.txt","r") as f:
    print(f.readlines())
    #or
    f.seek(0)
    for line in f:
        print(line)
