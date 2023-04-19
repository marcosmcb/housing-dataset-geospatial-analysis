## Installation

In order to run this program, please make sure you execute the following commands:

```bash
virtualenv venv
source venv/bin/activate  
pip3 install -r requirements.txt
```

## How to run it

### Housing dataset collection

Run the scripts in the following order:

1. `collector.py` must be run first as it will perform the data collection
    
    * Make sure to change the directory or create a brand new one.
    
    * For the collector script it may be necessary to make a few updates on the **daftlistings** library as it cannot handle null values for certain fields.
    
2. `combine_datasets.py` should be run next in order to combine the dataset created for each neighborhood in the previous step
    * Make sure you use the directory / files created in the previous step


### SocioEconomic datasets

The socio-economic datasets were obtained using a scripts for webscrapping government webpages, but also some public APIs.

For instance:

1. `get_train_stations.py` was created to query the Irish Rail API and collect all train stations in Ireland.

2. `google_geolocation.py` was used to hydrate some datasets - schools, hospitals and universities with latitude and longitude information by calling the Geocoding API from Google.

3. `web_scrapper_garda_stations.py` was created to webscrape the garda.ie website, neverhteless it makes use of a query response from the website that is store in _input_datasets/response_garda.txt_ folder.

4. `web_scrapper_ireland_schools.py` was utilised to webscrape the schools directory in the gov.ie website.


### Known bugs

If running these scripts on a Mac M1 (ARM chip), there have been problems installing packages like numpy which is required for _combine_datasets.py_ script.

_This is issue is being worked on however._