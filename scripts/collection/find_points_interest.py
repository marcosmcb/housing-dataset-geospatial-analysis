import pandas as pd
from pprint import pprint
import os
from turtle import distance
import googlemaps
import time

def miles_to_meters(miles):
    try:
        return miles * 1_609.344
    except:
        return 0

API_KEY = open('API_KEY.txt').read()

print(API_KEY)

map_client = googlemaps.Client(API_KEY)
location_name = (53.331949, -6.280380)
distance = miles_to_meters(5)
search_string = "university"

business_list = []

response = map_client.places_nearby(
    location=location_name,
    keyword=search_string,
    radius=distance
)

business_list.extend(response.get("results"))
next_page_token = response.get("next_page_token")

# print(response.get("results"))
# while next_page_token:
#     time.sleep(2)
#     response = map_client.places_nearby(
#         location=location_name,
#         keyword=search_string,
#         radius=distance
#     )

#     business_list.extend(response.get("results"))
#     next_page_token = response.get("next_page_token")


df = pd.DataFrame(business_list)
df.to_excel('universities_irl.xlsx', index=False)