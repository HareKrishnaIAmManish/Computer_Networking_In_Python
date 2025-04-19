def PrintExceptionTree(ExceptionClass, level = 0):
    if(level>1):
     print("  |"*(level-1),end="") #end=""doesnot go to a newline
    if(level>0):
     print("  +---",end="")
    print(ExceptionClass.__name__)
    for subclass in ExceptionClass.__subclasses__():
       PrintExceptionTree(subclass,level+1)
PrintExceptionTree(BaseException)


