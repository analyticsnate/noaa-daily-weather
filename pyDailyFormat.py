import pandas as pd

class dailyFile:
    """

    """
    self.colsList = ['ID','YEAR','MONTH','ELEMENT']
    self.widthsList = [11,4,2,4]

    def __init__(self,f):
        """
        constructor
        """
        self.dly = f

        # add VALUE(n), MFLAG(n), QFLAG(n), and SFLAG(n) for each day of the month# add V 
        for n in range(1,32):
            
            # append column names to colsList
            self.colsList.append('VALUE{}'.format(n))
            self.colsList.append('MFLAG{}'.format(n))
            self.colsList.append('QFLAG{}'.format(n))
            self.colsList.append('SFLAG{}'.format(n))
            
            # append column widths to widthsList
            self.widthsList.append(5)
            self.widthsList.append(1)
            self.widthsList.append(1)
            self.widthsList.append(1)

        # build dataframe
        self.dfRaw = pd.read_fwf(
                            f
                            ,header=None
                            ,widths=self.widthsList
                            ,names=self.colsList
                            ,index_col=False)

        self.df = pd.DataFrame(columns=['ID','YEAR','MONTH','ELEMENT','VALUE','DAY'])

        for i in range(1,32):
            df_Append = self.dfRaw.filter(['ID','YEAR','MONTH','ELEMENT','VALUE{}'.format(i)])
            df_Append.rename(columns={'VALUE{}'.format(i):'VALUE'},inplace=True)
            df_Append['DAY'] = i
            self.df = self.df.append(df_Append)