try:
    myfile=open("newfile.txt","wt")
    for i in range (1,10):
        myfile.write("line #" + str(i+1)+"\n")
    myfile.close()
except IOError as e:
    print("error is ",e)
            