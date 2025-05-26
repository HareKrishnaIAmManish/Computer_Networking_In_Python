import ftplib
FTP_SERVER_URL = 'ftp.be.debian.org'
DOWNLOAD_DIR_PATH = '/debian'
DOWNLOAD_FILE_NAME = 'README.mirrors.txt'
def ftp_fie_download(server,username):
    ftp_client=ftplib.FTP(server,username)
    ftp_client.cwd(DOWNLOAD_DIR_PATH)
    try:
        with open(DOWNLOAD_FILE_NAME,'wb') as file_handler:
            ftp_cmd='RETR %s' %DOWNLOAD_FILE_NAME
            ftp_client.retrbinary(ftp_cmd,file_handler.write)
            ftp_client.quit()
    except Exception as e:
        print("File could not be downloaded because",e)
if __name__=='__main__':
    ftp_fie_download(server=FTP_SERVER_URL,username='anonymous')
