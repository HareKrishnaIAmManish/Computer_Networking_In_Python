import subprocess
# print(subprocess.Popen(["python","--version"]))
process=subprocess.Popen(["python","--version"])
process.terminate()
