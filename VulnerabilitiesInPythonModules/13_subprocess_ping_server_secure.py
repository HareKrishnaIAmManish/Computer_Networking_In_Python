import subprocess
def ping_secure(myserver):
    command_arguments=['ping','-c','1',myserver]
    return subprocess.Popen(command_arguments,shell=False)
print(ping_secure('8.8.8.8;rm -rf /'))