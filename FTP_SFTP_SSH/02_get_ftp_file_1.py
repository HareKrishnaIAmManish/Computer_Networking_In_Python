from ftplib import FTP
def writeData(data):
    file_descryptor.write(data+'\n')
ftp_client=FTP('ftp.be.debian.org')
ftp_client.login()
ftp_client.cwd('/debian/tools/')
file_descryptor=open('loadlin.txt','wt')
ftp_client.retrlines('RETR loadlin.txt',writeData)
file_descryptor.close()
ftp_client.quit()
