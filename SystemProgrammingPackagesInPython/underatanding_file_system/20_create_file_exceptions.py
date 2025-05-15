def main():
    try:
        with open("test.txt",'w') as f:
            f.write("this is a test file")
    except IOError as e:
        print("exception caught",e)
    else:
        print("file written successfully")
if __name__=="__main__":
    main()
