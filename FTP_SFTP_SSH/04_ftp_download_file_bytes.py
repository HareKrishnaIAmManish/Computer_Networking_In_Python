from ftplib import FTP
ftp_client=FTP('ftp.be.debian.org')
ftp_client.login()
ftp_client.cwd('/video.fosdem.org')
ftp_client.voidcmd("TYPE I")
datasock,estsize=ftp_client.ntransfercmd("RETR README.txt")
print("datasock is of type",type(datasock))
print("estsize is of type",type(estsize))
transbytes=0
with open('READMEE.txt','wb') as file_descrypter:
    while True:
        buffer=datasock.recv(2048)
        if not len(buffer):
            break
        file_descrypter.write(buffer)
        transbytes+=len(buffer)
        print("Bytes received",transbytes,"Total",(estsize,100.0*float(transbytes)/float(estsize)),str('%'))
datasock.close()
ftp_client.quit()

