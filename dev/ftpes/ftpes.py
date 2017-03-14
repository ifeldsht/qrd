from ftplib import FTP_TLS
import sys

ftps = FTP_TLS('209.99.16.94')
ftps.login(sys.argv[1], sys.argv[2])  
ftps.prot_p()  
ftps.retrlines('LIST')

#ftps.storbinary('STOR aaa.txt', open('ftpes.py'))
with open(sys.argv[3],"wb") as f:
    ftps.retrbinary('RETR ' + sys.argv[3], f.write)

ftps.close()
