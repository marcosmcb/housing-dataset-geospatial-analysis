## Installation

In order to run this program, please make sure you execute the following commands:

```bash

virtualenv venv
source venv/bin/activate  
pip3 install -r requirements.txt
```


## How to run it

Run the scripts in the following order:

- _collector.py_ must be run first as it will perform the data collection
    * Make sure to change the directory or create a brand new one.
    
- _combine_datasets.py_ should be run next in order to combine the dataset created for each neighborhood in the previous step
    * Make sure you use the directory / files created in the previous step
    
- _find_point_interest.py_ can be run in order to interact with the Google Places API