import urllib.parse
import requests
import csv
import sys
import time

API_KEY = open('API_KEY.txt').read()

def writeDictToCSV(rows, headers, filename):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def call_google_maps(address):
    query = urllib.parse.quote(address)

    try:
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + query + '&key=' + API_KEY)

        result_payload = response.json()
        geolocation = result_payload['results'][0]['geometry']['location']

        return {
            "latitude": geolocation["lat"],
            "longitude": geolocation["lng"]
        }
    except Exception as e:
        print("Failed to parse address " + str(e))
        return {
            "latitude": "NA",
            "longitude": "NA"
        }

def find_univesities_geolocation(filename):
    rows = []
    headers = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for row in reader:
            geolocation = call_google_maps(row["name"])            
            row.update(geolocation)
            rows.append(row)
            time.sleep(1)
    headers.append("latitude")
    headers.append("longitude")
    return {
        "rows": rows,
        "headers": headers
    }
    
def find_schools_geolocation(filename):
    rows = []
    headers = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for row in reader:
            address = ",".join([row["name"], row["city"], row["postcode"]])
            geolocation = call_google_maps(address)            
            row.update(geolocation)
            rows.append(row)
            time.sleep(0.25)
    headers.append("latitude")
    headers.append("longitude")
    return {
        "rows": rows,
        "headers": headers
    }

def find_hospitals_geolocation(filename):
    rows = []
    headers = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for row in reader:
            address = ",".join([row["name"], row["address"], row["eircode"]])
            geolocation = call_google_maps(address)            
            row.update(geolocation)
            rows.append(row)
            time.sleep(0.1)
    headers.append("latitude")
    headers.append("longitude")
    return {
        "rows": rows,
        "headers": headers
    }

            


if __name__ == "__main__":
    dataset = sys.argv[1]
    if (dataset == "university"):
        result = find_univesities_geolocation("universities.csv")
        writeDictToCSV( result["rows"], result["headers"], "universities-geolocation.csv" )
    elif (dataset == "schools"):
        result = find_schools_geolocation("schools_addresses.csv")
        writeDictToCSV( result["rows"], result["headers"], "schools-geolocation.csv" )
    elif (dataset == "hospitals"):
        result = find_hospitals_geolocation("hospitals.csv")
        writeDictToCSV( result["rows"], result["headers"], "hospitals-geolocation.csv" )
    else:
        raise Exception("Invalid Argument")