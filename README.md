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
        
        
    - ghcnd-stations-cleansed.csv is the dataset used in this Tableau Dashboard
    <div class='tableauPlaceholder' id='viz1533514354666' style='position: relative'><noscript><a href='#'><img alt='GHCN Station Map DashboardDescription: this map visualization shows all weather stations in the GLOBAL HISTORICAL CLIMATOLOGY NETWORK (GHCN).Author: Nate Muth | nmuth87@gmail.com | 7&#47;29&#47;2018 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NO&#47;NOAADailyWeatherProject&#47;GHCNStationMapDashboard&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='NOAADailyWeatherProject&#47;GHCNStationMapDashboard' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NO&#47;NOAADailyWeatherProject&#47;GHCNStationMapDashboard&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1533514354666');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1280px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1280px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
5. Open noaa-