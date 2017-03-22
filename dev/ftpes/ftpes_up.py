from ftplib import FTP_TLS
import sys

ftps = FTP_TLS('209.99.16.94')
ftps.login(sys.argv[1], sys.argv[2])  
ftps.prot_p()  

ftps.storbinary('STOR '+sys.argv[3], open(sys.argv[3]))

ftps.retrlines('LIST')
ftps.close()
