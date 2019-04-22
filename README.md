# NOAA Datasets Python Library
by: Nate Muth (Omaha, NE)

### How to get started
```
# import the noaa_datasets library
import noaa_datasets

# load the stations dataset and show the first five rows
stations_dataset = noaa_datasets.Stations()
stations_dataset.df.head()

# load the inventory dataset and show the first five rows
inventory_dataset = noaa_datasets.Inventory(stations_dataset)
inventory_dataset.df.head()
```

### Example Projects
1. Tutorial Demo
1. Epply Snow Dataset
2. Last Day of Freezing Temps

