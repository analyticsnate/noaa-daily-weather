import pandas as pd 

class daily_file:
    """
    """
    cols_list = ['ID','YEAR','MONTH','ELEMENT']
    widths_list = [11,4,2,4]

    def __init__(self,f):
        """
        constructor
        """
        self.dly = f

        # add VALUE(n), MFLAG(n), QFLAG(n), and SFLAG(n) for each day of the month# add V
        for n in range(1,32):

            # append column names to colsList
            self.cols_list.append('VALUE{}'.format(n))
            self.cols_list.append('MFLAG{}'.format(n))
            self.cols_list.append('QFLAG{}'.format(n))
            self.cols_list.append('SFLAG{}'.format(n))

            # append column widths to widthsList
            self.widths_list.append(5)
            self.widths_list.append(1)
            self.widths_list.append(1)
            self.widths_list.append(1)

        # build dataframe
        self.df_raw = pd.read_fwf(
                            f
                            ,header=None
                            ,widths=self.widths_list
                            ,names=self.cols_list
                            ,index_col=False)

        self.df = pd.DataFrame(columns=['ID','YEAR','MONTH','ELEMENT','VALUE','DAY'])

        for i in range(1,32):
            df_append = self.df_raw.filter(['ID','YEAR','MONTH','ELEMENT','VALUE{}'.format(i)])
            df_append.rename(columns={'VALUE{}'.format(i):'VALUE'},inplace=True)
            df_append['DAY'] = i
            self.df = self.df.append(df_append)
