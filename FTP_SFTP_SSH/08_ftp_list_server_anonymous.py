import ftplib
FTP_SERVER_URL='ftp.be.debian.org'
DOWNLOAD_DIR_PATH = '/debian-cd/current/source/bt-dvd/'
def check_anonymous_connection(host,path):
    with ftplib.FTP(host,user="anonymous") as connection:
        print("Welcome to ftp server ",connection.getwelcome())
        for name,details in connection.mlsd(path):
            print("----------------------------------------")
            print(details)
            print((name,details['type'],details.get('size')))
            print("----------------------------------------")
if __name__ =='__main__':
        check_anonymous_connection(FTP_SERVER_URL,DOWNLOAD_DIR_PATH)        