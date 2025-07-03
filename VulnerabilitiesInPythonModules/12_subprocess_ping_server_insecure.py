import subprocess
def ping_insecure(myserver):
    return subprocess.Popen('ping -c 1 %s' % myserver,shell=True)
print(ping_insecure('8.8.8.8 & touch file2'))
