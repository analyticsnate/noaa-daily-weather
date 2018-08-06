# README
---- GLOBAL HISTORICAL CLIMATOLOGY NETWORK (GHCN) PROJECT
by: Nate Muth (Omaha, NE)

Welcome to the GitHub repository for the GHCN Project. Let's create things with data!

Technology Used:
- GitHub | <a href="https://desktop.github.com/">Link</a>
- Anaconda | <a href="https://conda.io/docs/download.html">Link</a><br>
    <br>
    Includes:
    - Python
    - Jupyter Notebooks
    - pandas DataFrames
    
- Tableau Public | <a href="https://public.tableau.com/en-us/s/">Link</a>

To follow along with this project, you'll need a basic understanding of those technologies.

To get started:
1. Clone this repository
2. Open noaa-daily-retrieve-files-ftp.ipynb in a Jupyter Notebook
3. Run all the cells in this Notebook
    - This will download the raw data files from the public GHCN FTP site: ftp.ncdc.noaa.gov/pub/data/ghcn/daily
        Default Files Included:
        - ghcnd-stations.txt
        - ghcnd-countries.txt
        - ghcnd-states.txt
        - ghcnd-inventory.txt
        
    - The config section gives control over which files to download
    - Study this Notebook to gain an understanding of using FTPs in python
    
4. Open noaa-daily-stations-prep.ipynb and run all of its cells
    - This preps data about the weather stations in the GHCN
    - Files created from this code
        - ghcnd-stations-cleansed.csv
        
        
    - ghcnd-stations-cleansed.csv is the dataset used in this Tableau Dashboard | <a href='https://public.tableau.com/profile/nate.muth#!/vizhome/NOAADailyWeatherProject/GHCNStationMapDashboard'>Link</a>
    ![alt text]('https://github.com/nmuth87/noaa-daily-weather/blob/master/Images/ghcn_station_map_dashboard.PNG')
    
5. Open noaa-