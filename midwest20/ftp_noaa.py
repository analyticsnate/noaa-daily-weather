from ftplib import FTPs

class ftp_noaa:

    def __init__(self,folder='pub/data/ghcn/daily'):
        """
        NOAA FTP Wrapper

        Params:
        -------
        folder : str
        - folder to change directory
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



    