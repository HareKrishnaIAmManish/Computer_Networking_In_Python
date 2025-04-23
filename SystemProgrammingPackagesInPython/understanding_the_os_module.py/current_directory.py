import os
pwd=os.getcwd()
print(pwd)
list_directory=os.listdir(pwd)
print("the path contains")
for directory in list_directory:
    print(directory)



