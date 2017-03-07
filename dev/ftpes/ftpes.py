from ftplib import FTP_TLS
import sys

ftps = FTP_TLS('209.99.16.94')
ftps.login('usr', 'pwd')  
ftps.prot_p()  
ftps.retrlines('LIST')

ftps.storbinary('STOR aaa.txt', open('ftpes.py'))
#filename = 'remote_filename.bin'
#print 'Opening local file ' + filename
#myfile = open(filename, 'wb')
#ftps.retrbinary('RETR %s' % filename, myfile.write)

ftps.close()
