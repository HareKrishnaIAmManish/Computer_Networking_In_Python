import os
from subprocess import call
# import subprocess
# print(help(subprocess.call))
print("current path-> ",os.getcwd())
print("path environment variable",os.getenv("PATH"))
print("list files using the os module:")
os.system("ls -la")
print("list files using the subprocess module: ")
# call(["ls"])
call(["ls","-la"])
