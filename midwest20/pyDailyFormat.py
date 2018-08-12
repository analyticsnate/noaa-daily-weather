import pandas as pd
from datetime import datetime

def dailyFile(f):

    colsList = ['ID','YEAR','MONTH','ELEMENT']
    widthsList = [11,4,2,4]

    # add VALUE(n), MFLAG(n), QFLAG(n), and SFLAG(n) for each day of the month# add V 
    for n in range(1,32):
        
        # append column names to colsList
        colsList.append('VALUE{}'.format(n))
        colsList.append('MFLAG{}'.format(n))
        colsList.append('QFLAG{}'.format(n))
        colsList.append('SFLAG{}'.format(n))
        
        # append column widths to widthsList
        widthsList.append(5)
        widthsList.append(1)
        widthsList.append(1)
        widthsList.append(1)

    # build dataframe
    dfRaw = pd.read_fwf(
                        f
                        ,header=None
                        ,widths=widthsList
                        ,names=colsList
                        ,index_col=False)

    df = pd.DataFrame(columns=['ID','YEAR','MONTH','ELEMENT','VALUE','DAY'])

    for i in range(1,32):
        df_Append = dfRaw.filter(['ID','YEAR','MONTH','ELEMENT','VALUE{}'.format(i)])
        df_Append.rename(columns={'VALUE{}'.format(i):'VALUE'},inplace=True)
        df_Append['DAY'] = i
        df = df.append(df_Append)

    # convert date elements into a date string
    df['WeatherDate'] = df.apply(getDate,axis=1)

    # remove date element columns
    df.drop(['YEAR','MONTH','DAY'],inplace=True)

    return df

def getDate(row):
    return '{}/{}/{}'.format(row['MONTH'],row['DAY'],row['YEAR'])