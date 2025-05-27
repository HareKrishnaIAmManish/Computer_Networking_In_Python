from ftplib import FTP
def writeData(data):
    file_descryptor.write(data+"\n")
ftp_client=FTP('ftp.be.debian.org')
ftp_client.login()
ftp_client.cwd('/debian/tools/')
with open('loadlin.txt','wt') as file_descryptor:
    ftp_client.retrlines('RETR loadlin.txt',writeData)
ftp_client.close()
