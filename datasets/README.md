# Dataset Files

This directory contains all datasets used in this machine learning and data analysis project. The datasets are grouped by category and the following is a description of each dataset:

## Housing datasets

These datasets contain information about the houses collected from the Daft.ie API.

### `houses_per_town`

This directory contains the houses collected for each town or neighbourhood in Ireland - refered as locations in the Daft.ie API. Those files are in CSV format and hold all the variables available from the API. Some of those files may be empty.

This data was collected using the daftlistings *2.0.2* python library. [pypi daftlistings](https://pypi.org/project/daftlistings/).

### `house_listings_all.csv`

This file is a result of joining all the files from the **houses-per-town** directory. This dataset is in CSV format and contains over 100327 rows.

### `ireland_houses_cleaned.Rda`

This dataset is the result of the pre-processing and cleaning stages of **house_listings_all.csv** dataset.

The dataset is stored in R dataframe format and it contains 9009 observations.

The dataset has the following fields:

| Variable      | Description |
| -----------   | ----------- |
| address       | A long form of the property address |
| bathrooms     | The number of bathrooms in this property |
| bedrooms      | The number of bedrooms in this property |
| berRating     | BER Rating of this property, i.e. A1, B2  |
| county        | The county the property is in. Examples: "Co. Wicklow", "Co. Kerry"        |
| latitude      | The latitude of the property        |
| location      | A short form of the property address area, i.e. Dublin 1, Co. Dublin    |
| longitude     | The longitude of the property    |
| price         | The price of the property, in euro €  |
| propertyType  | The type of the property, i.e. Apartment, End of Terrace, Semi-D, Terrace  |
| size          | The size of the property in square meters      |
| townOrNeighbourhood     | The town or neighbourhood where is the property    |


## Geospatial and Shape Files of Ireland

### `shapefile_ireland`

This directory contains the shapefiles for the country of Ireland.

Those shapefiles were obtained from the GADM maps and data portal. [Select Ireland in the dropdown list and download the files](https://gadm.org/download_country.html)


### `ireland_counties.geojson`

This file was obtained from a public repository on github and it contains the geo polygons of the irish counties in geojson format.

The file was obtained from the following repository [brendanjodowd/maps/lea_166.geojson](https://github.com/brendanjodowd/maps/blob/main/lea_166.geojson).


## Education

In this directory, the datasets on the universities and schools of Ireland along with their geocoordinates can be found.

### `schools.csv`

This file contains the *latitude* and *longitude* information of over **3596** schools in Ireland.

The dataset is in CSV format and it was obtained via web scrapping from the [schools directory on the gov.ie](https://www.gov.ie/en/directory/category/495b8a-schools/?page=1) portal.


### `universities.csv`

This file contains geolocation information about the 22 universities and colleges in Ireland. This information was manually collected from the [Education in Ireland](https://www.educationinireland.com/en/Where-can-I-study-/) website and subsequently updated with the information about the *latitude* and *longitude* of each university.

## Health

### `hospitals.csv`

This dataset contains information about 38 hospitals in Ireland. This dataset may not represent the full number of hospitals in Ireland, however no other reliable data source was found to collect such data. The dataset was updated so that it contained the latitude and longitude of each hospital in Ireland in WGS84 format.

The dataset is in CSV format and was obtained from the **HSE - Health Service Executive** page on [data.gov.ie Open Data portal](https://data.gov.ie/dataset/list-of-hospitals-in-ireland/resource/f6727f58-a6bc-45f9-9657-84c9eecfd5b7)


## Police

### `garda_stations.csv`

This file contains information about each garda station in Ireland. There are 568 samples in this dataset.

The dataset is stored in CSV format and it was obtained by web scrapping and querying the API used in the [garda.ie directory](https://www.garda.ie/en/contact-us/station-directory/).


## Public transport

In this directory, the datasets for all bus stops and train stations in the island of Ireland (Northern Ireland and the Republic of Ireland) can be found.

### `bus_stops_ireland.csv`

In this file you can find all 16352 bus stops in Ireland, among many variables in the dataset, it is possible to find latitude and longitude for each bus stop. 

This dataset is stored in CSV format and it was obtained from the **National Transport Ireland** page on [data.gove.ie Open Data portal](https://data.gov.ie/dataset/national-public-transport-access-nodes-naptan)

### `train_stations.csv`

This file contains information about 168 train stations in the island of Ireland. For each train station it is possible to find the latitude and longitude of each one.

The dataset is stored in CSV format and was obtained by querying the **Irish Rail V1** [Get All Stations API](http://api.irishrail.ie/realtime/realtime.asmx?op=getAllStationsXML).