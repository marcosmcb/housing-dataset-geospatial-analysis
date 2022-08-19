import csv
import json
from datetime import datetime
from csv import DictWriter
from daftlistings import Daft, Location, SearchType, PropertyType, Listing


DATASET_FOLDER = "../../datasets/"

PROPERTY_TYPES = [ PropertyType.APARTMENT, PropertyType.BUNGALOW, PropertyType.DETACHED_HOUSE, 
    PropertyType.DUPLEX, PropertyType.END_OF_TERRACE_HOUSE, PropertyType.HOUSE, 
    PropertyType.SEMI_DETACHED_HOUSE, PropertyType.STUDIO_APARTMENT, PropertyType.TERRACED_HOUSE, 
    PropertyType.TOWNHOUSE ]


def open_csv(filename):
    file = open(filename, "a")
    dict_fields = ["id", "daftShortcode", "title", "price", 
        "size_meters_squared", "propertySize", "bedrooms", 
        "bathrooms", "propertyType", "publishDate", 
        "ber_rating", "ber_code", "ber_epi", 
        "latitude", "longitude", "category", 
        "location", "url_link"]
    writer = csv.DictWriter(file, fieldnames=dict_fields, extrasaction='ignore', delimiter = ',')
    writer.writeheader()
    return file, writer

def close_csv(file):
    file.close()

def format_price(price_str):
    if price_str is None: return ""
    try:
        return float(price_str.replace("€","").replace(",",""))
    except Exception as err:
        print("price parsing exception", err)
        return price_str
    

def format_bedroom(bedroom):
    if bedroom is None: return ""
    try:
        return int(bedroom.lower().replace("bed", ""))
    except Exception as err:
        print("bedroom parsing exception", err)
        return bedroom
    

def format_bathroom(bathroom):
    if bathroom is None: return ""
    try:
        return int(bathroom.lower().replace("bath", ""))
    except Exception as err:
        print("bathroom parsing exception", err)
        return bathroom

def get_date_from_timestamp(timestamp):
    return datetime.fromtimestamp(int(timestamp) / 1000).date()


def get_property_value(listing_dict: dict, property):
    if property in listing_dict:
        return listing_dict[property]
    return ""


def create_dict(listing: Listing, location: Location):
    listing_dict = listing.as_dict()
    return { 
        "id": get_property_value(listing_dict, "id"), 
        "daftShortcode": get_property_value(listing_dict, "daftShortcode"), 
        "title": get_property_value(listing_dict, "title"), 
        "price": format_price(get_property_value(listing_dict, "price")), 
        "size_meters_squared": listing.size_meters_squared,
        "propertySize": get_property_value(listing_dict, "propertySize"),
        "bedrooms": format_bedroom(listing.bedrooms),
        "bathrooms": format_bathroom(listing.bathrooms),
        "propertyType": get_property_value(listing_dict, "propertyType"),
        "publishDate": get_date_from_timestamp(get_property_value(listing_dict, "publishDate")),
        "ber_rating": get_property_value(get_property_value(listing_dict, "ber"), "rating"),
        "ber_code": get_property_value(get_property_value(listing_dict, "ber"), "code"),
        "ber_epi": get_property_value(get_property_value(listing_dict, "ber"), "epi"),
        "latitude": listing.latitude,
        "longitude": listing.longitude,
        "category": listing.category,
        "location": location.name,
        "url_link": listing.daft_link
    }

def write_dict_to_csv(writer: DictWriter, listings: list):    
    writer.writerows(listings)


def build_search(location: Location, propertyType: PropertyType):
    daft = Daft()
    daft.set_location(location)
    daft.set_search_type(SearchType.RESIDENTIAL_SALE)
    daft.set_property_type(propertyType)

    listings = daft.search()
    return listings

def flatten(list_of_lists):
    out = []
    for sublist in list_of_lists:
        out.extend(sublist)
    return out



def perform_searches():
    
    for location in Location:
        print('{:15} = {}'.format("Searching", location.name))

        listings_of_listings = [build_search(location, property) for property in PROPERTY_TYPES]

        print('{:15} = {}'.format("Finished Searching", location.name))
        listings = flatten(listings_of_listings)

        file, writer = open_csv(DATASET_FOLDER + location.name + ".csv")
        dict_listings = [create_dict(listing, location) for listing in listings]

        write_dict_to_csv(writer, dict_listings)
        close_csv(file)


perform_searches()
