## Installation

In order to run this program, please make sure you execute the following commands:

```bash
virtualenv venv
source venv/bin/activate  
pip3 install -r requirements.txt
```

## How to run it

Run the scripts in the following order:

1. _collector.py_ must be run first as it will perform the data collection
    
    * Make sure to change the directory or create a brand new one.
    
    * For the collector script it may be necessary to make a few updates on the **daftlistings** library as it cannot handle null values for certain fields.
    
2. _combine_datasets.py_ should be run next in order to combine the dataset created for each neighborhood in the previous step
    * Make sure you use the directory / files created in the previous step
    
3. _find_point_interest.py_ can be run in order to interact with the Google Places API


## Known bugs

If running these scripts on a Mac M1, there have been problems installing packages like numpy and googlemaps which are required for _combine_datasets.py_ and _find_points_interest.py_ scripts respectively.

_This is issue is being worked on however._