import csv
import xmltodict
import requests


def get_train_stations_xml():
    response = requests.get('http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML')
    train_stations_xml = xmltodict.parse(response.content)
    return train_stations_xml

def writeDictToCSV(rows, headers, filename):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    stations_xml = get_train_stations_xml()
    stations = stations_xml["ArrayOfObjStation"]["objStation"]
    writeDictToCSV(stations, stations[0].keys(), "trains_stations.csv")