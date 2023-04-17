import requests
from bs4 import BeautifulSoup
import csv
import time


def writeDictToCSV(schoolRows):
    fieldnames = ['name', 'addressLine', 'city', 'neighboorhoud', 'postcode']

    with open('schools_addresses.csv', 'w', encoding='UTF8', newline='') as school_dataset:
        writer = csv.DictWriter(school_dataset, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(schoolRows)

def parse_address(address):
    address_tokens = address.split(",")
    address_tokens.reverse()
    addressLine = ''
    city = ''
    neighboorhoud = ''
    postcode = ''
    try:
        addressLine = address_tokens.pop().strip()
        city = address_tokens.pop().strip()
        neighboorhoud = address_tokens.pop().strip()
        postcode = address_tokens.pop().strip()
    except Exception as e:
        print("Failed to parse address " + str(e))

    return {
        "addressLine": addressLine,
        "city": city,
        "neighboorhoud": neighboorhoud,
        "postcode": postcode
    }


def scrape_webpage():
    data = []
    START_PAGE = 1
    LAST_PAGE = 401

    for page_num in range(START_PAGE, LAST_PAGE, 1):
        print("Iteration " + str(page_num))
        page = requests.get('https://www.gov.ie/en/directory/category/495b8a-schools/?page=' + str(page_num)) # Getting page HTML through request
        soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup

        all_span_tags = soup.findAll("span", class_="glyphicon glyphicon-map-marker")

        for x in range(len(all_span_tags)):
            school_name = soup.select('div.row.margin-bottom-sm > div > ul > li:nth-child(' + str(x) + ') > a')
            if (len(school_name) == 0):
                continue

            school_address = parse_address(all_span_tags[x].find_next(string=True).strip())
            school_dict = { 'name': school_name[0].text.strip() }
            school_dict.update(school_address)
            data.append( school_dict )
        time.sleep(10)

    return data

if __name__ == "__main__":
    csv_rows = scrape_webpage()
    writeDictToCSV(csv_rows)