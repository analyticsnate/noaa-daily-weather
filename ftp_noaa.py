from ftplib import FTP

class ftp_noaa():

    def __init__(self, folder='pub/data/ghcn/daily'):
        """
        NOAA FTP Wrapper
        Params:
        -------
        folder : str
        - folder to change directory
        """
        self.ftp = FTP('ftp.ncdc.noaa.gov')
        self.ftp.login()
        self.ftp.cwd(folder)

    def retrieve_file(self, file_name, folder_name=None):
        """
        Copies file from NOAA FTP site to local directory
        Params:
        -------
        fileName : str
        - name of file to be copied from NOAA FTP
        """
        if folder_name is not None:
            local_file = open((folder_name + file_name), 'wb')
        else:
            local_file = open((file_name), 'wb')
        
        self.ftp.retrbinary('RETR {}'.format(file_name),local_file.write,8*102)

    def quit(self):
        self.ftp.quit()
