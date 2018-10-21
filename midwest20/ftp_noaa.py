from ftplib import FTP
import pandas as pd
import os

class ftp_noaa:

    def __init__(self,folder=''):
        """
NOAA FTP Wrapper

Params:
-------
folder : str
- folder to change directory
- default is 'pub/data/ghcn/daily'
        """
        self.ftp = FTP('ftp.ncdc.noaa.gov')
        self.ftp.login()
        self.ftp.cwd('pub/data/ghcn/daily{}'.format(folder))

    def retrieveFile(self,fileName):
        """
Copies file from NOAA FTP site to local directory

Params:
-------
fileName : str
- name of file to be copied from NOAA FTP
        """
        localFile = open((fileName), 'wb')
        self.ftp.retrbinary('RETR {}'.format(fileName),localFile.write,8*102)

    def quit(self):
        self.ftp.quit()



    