# noaa_datasets.py
#
# NOAA Datasets Python Library
# This library contains classes and methods for interacting with datasets from the
# NATIONAL OCEANIC AND ATMOSPHERIC ADMINISTRATION (NOAA) GLOBAL HISTORICAL CLIMATOLOGY NETWORK (GHCN).
#
# The GHCN project captures weather measurements from thousands of weather stations 
# thoughout the world, then saves the data in a standardized format for analysis.
#
# This standardized format is good for storage size, but not human interaction, which is
# where this python library helps. The classes and methods in this library automate downloading
# GHCN data from their public FTP, then formats the data so that it's easier to analyze in tools 
# like Tableau and Power BI.
# 
# Link: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/

import pandas as pd 
import noaa_ftp

class DailyFile:
    """
    TODO: add docstring
    """
    cols_list = ['ID','YEAR','MONTH','ELEMENT']
    widths_list = [11,4,2,4]

    def __init__(self, station_id):
        self.ftp = noaa_ftp.NoaaFTP('pub/data/ghcn/daily/all')
        print(f'Retrieving {station_id}.dly')
        self.ftp.retrieve_file(f'{station_id}.dly', 'data/')
        self.ftp.quit()

        # add VALUE(n), MFLAG(n), QFLAG(n), and SFLAG(n) for each day of the month
        print(f'Transposing {station_id} dataset')
        for n in range(1,32):

            # append column names to colsList
            self.cols_list.append(f'VALUE{n}')
            self.cols_list.append(f'MFLAG{n}')
            self.cols_list.append(f'QFLAG{n}')
            self.cols_list.append(f'SFLAG{n}')

            # append column widths to widthsList
            self.widths_list.append(5)
            self.widths_list.append(1)
            self.widths_list.append(1)
            self.widths_list.append(1)

        # build dataframe
        self.df_raw = pd.read_fwf(
                            f'data/{station_id}.dly'
                            ,header=None
                            ,widths=self.widths_list
                            ,names=self.cols_list
                            ,index_col=False)

        self.df = pd.DataFrame(columns=['ID','YEAR','MONTH','ELEMENT','VALUE','DAY'])

        for i in range(1,32):
            df_append = self.df_raw.filter(['ID','YEAR','MONTH','ELEMENT',f'VALUE{i}'])
            df_append.rename(columns={f'VALUE{i}':'VALUE'},inplace=True)
            df_append['DAY'] = i
            self.df = self.df.append(df_append)

        # --apply data prep operations
        print('Applying data prep operations')

        # 1. change ID column name to StationID
        self.df = self.df.rename(columns={'ID': 'StationID'})

        # 2. change datatype of value to double
        self.df['VALUE'] = self.df['VALUE'].astype('float')

        # 3. filter out -9999 values
        self.df = self.df[ self.df['VALUE']>-9999 ]

        print('Success!')

    def mm_to_inches(self, row):
        """
        converts the VALUE from millimeters to inches
        because murica is "special"
        """
        return row['VALUE'] / 25.4

    def c_to_f(self, row):
        # (0°C × 9/5) + 32 = 32°F
        return ( ((((row['VALUE']/10) * 9) / 5) + 32))

    def winter_season(self, row):
        """
        formats the YEAR field to be like the winter of 90-91, 03-04
        these years in this format go from June to May
        """
        if row['MONTH'] < 6:
            return str(row['YEAR'] - 1)[2:4] + '-' + str(row['YEAR'])[2:4]
        else:
            return str(row['YEAR'])[2:4] + '-' + str(row['YEAR'] + 1)[2:4]

class Stations:
    """
    Pulls down the Stations dataset from the NOAA FTP site, and
    normalizes states and countries data

    Params:
    -------
    debug : boolean
    Set to True to show debug print messages while using this class
    """

    def __init__(self, debug=False):

        self.ftp = noaa_ftp.NoaaFTP()
        self.debug = debug

        for f in ['ghcnd-stations.txt', 'ghcnd-states.txt', 'ghcnd-countries.txt']:
            if self.debug:
                print(f'Retrieving {f}')
            self.ftp.retrieve_file(f, 'data/')
        self.ftp.quit()

        # TODO: add error handling for reading the file
        if self.debug:
            print('Reading ghcnd-stations.txt')
        self.df = pd.read_fwf('data/ghcnd-stations.txt', header=None, delimiter=' '
                     , widths=[12,9,10,7,3,31,4,4,6]
                     , names=['StationID', 'Latitude', 'Longitude', 'Elevation'
                            ,'State', 'StationName', 'GSN_Flag', 'HCN_CRN_Flag'
                            ,'WMO_ID']
                     , dtypes={'WMO_ID':object},index_col='StationID')

        if self.debug:
            print('Reading ghcnd-countries.txt')
        self.countries = pd.read_fwf('data/ghcnd-countries.txt', header=None,
                            delimiter=' ', names=['CountryCode','CountryName'])

        if self.debug:
            print('Reading ghcnd-states.txt')
        self.states = pd.read_fwf('data/ghcnd-states.txt', header=None,
                            delimiter=' ', names=['State','StateName'])

        # --apply dataprep operations here
        if self.debug:
            print('Applying data prep operations to enrich dataset')

        # 1. slice country code from the StationID value
        self.df['CountryCode'] = self.df.apply(self.slice_country_code, axis=1)

        # 2. merge this country code to the countries dataset
        self.df = self.df.reset_index().merge(self.countries, on='CountryCode', how='left').set_index('StationID')
        
        # 3. merge states dataset next
        self.df = self.df.reset_index().merge(self.states, on='State', how='left').set_index('StationID')

        # always display this
        print('Success!')

    def slice_country_code(self, row):
        """
        returns first two chars of Name field
        for NOAA data, this is the country code
        """
        return row.name[:2]

class Inventory:
    """
    Pulls down the Stations dataset from the NOAA FTP site, and
    normalizes states and countries data

    Params:
    -------
    Stations : Stations object
    TODO: add description of this

    debug : boolean
    Set to True to show debug print messages while using this class

    Example:
    --------
    > import noaa_datasets
    > stations_dataset = noaa_datasets.Stations()
    > inventory_dataset = noaa_datasets.Inventory(stations_dataset)
    """

    def __init__(self, Stations, debug=False):

        self.ftp = noaa_ftp.NoaaFTP()
        self.debug = debug
        if self.debug:
            print('Retrieving ghcnd-inventory.txt')
        self.ftp.retrieve_file('ghcnd-inventory.txt', 'data/')
        self.ftp.quit()
        self.df_stations = Stations.df

        if self.debug:
            print('Reading ghcnd-inventory.txt')
        self.df_inventory = pd.read_fwf('data/ghcnd-inventory.txt', header=None, delimiter=' '
                         , widths=[12,9,10,5,5,5]
                         , names=['StationID', 'Latitude', 'Longitude', 'Element',
                                 'FirstYear', 'LastYear'])

        if self.debug:
            print('Merging with Stations dataset')
        self.df = self.df_inventory.filter(['StationID', 'Element', 'FirstYear', 'LastYear'])
        self.df = pd.merge(self.df, self.df_stations, how='left', left_on='StationID', right_index=True).reset_index()
        # self.df = self.df.drop('index')
        self.df['YearCount'] = self.df.apply(self.calc_year_count, axis=1)

        # always print this
        print('Success!')

    def calc_year_count(self, row):
        """
        returns the difference between the LastYear and FirstYear

        ex.
        Last Year = 2019
        First Year = 2008
        returns 11
        """
        return row['LastYear'] - row['FirstYear']

    def save_datasets(self):
        if self.debug:
            print('Saving ghcnd-inventory-cleansed.csv')
        self.df_inventory.to_csv('data/ghcnd-inventory-cleansed.csv', sep='\t')

        if self.debug:
            print('Saving ghcnd-stations-cleansed.csv')
        self.df_stations.to_csv('data/ghcnd-stations-cleansed.csv', sep='\t')

        if self.debug:
            print('Saving ghcnd-stations-inventory-cleansed.csv')
        self.df.to_csv('data/ghcnd-stations-inventory-cleansed.csv',sep='\t')



                     
