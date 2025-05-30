import pysftp
import getpass
HOSTNAME="localhost"
PORT=22
def sftp_getfiles(username,password,hostname=HOSTNAME,port=PORT):
    with pysftp.Connection(host=hostname,username=username,password=password) as sftp:
        print("connection successfully established with server...")
        sftp.cwd('/')
        list_directory=sftp.listdir_attr()
        for directory in list_directory:
            print("-----------------------------------------------------")
            print(directory.filename,directory)
            print("-----------------------------------------------------")
if __name__=="__main__":
    hostname=''
    port=22
    username=""
    password=""
    sftp_getfiles(username,password,hostname,port)
