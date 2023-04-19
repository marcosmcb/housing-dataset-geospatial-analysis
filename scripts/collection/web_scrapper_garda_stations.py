import html_to_json
import csv


def convert_html_to_json():
    response_html_format = open("response_garda_all.txt", "r")
    return html_to_json.convert(response_html_format.read())

def parse_garda_station_data(garda_station_data_rows):
    garda_station = {}
    for idx in range(len(garda_station_data_rows)):
        td = garda_station_data_rows[idx]["td"]
        if (len(td) < 2):
            continue
        
        if ("_value" in td[0] and "_value" in td[1]):            
            key = td[0]["_value"]
            value = td[1]["_value"]
            garda_station.update({
                key: value
            })
    
    return garda_station

        

def parse_root_div_element(element):
    body = element["html"][0]["body"]
    table = body[0]["table"]
    tr = table[0]["tr"]
    td = tr[1]["td"]
    second_table = td[0]["table"]
    second_tr = second_table[0]["tr"]
    return parse_garda_station_data(second_tr)
    

def parse_json_html_tree(output_json):
    all_garda_stations = []
    root_div = output_json["div"]
    for div_idx in range(len(root_div)):
        garda_station = parse_root_div_element(root_div[div_idx]["div"][0])
        all_garda_stations.append(garda_station)
    return all_garda_stations


def write_dict_to_csv(schoolRows):
    fieldnames = ['Station', 'Address', 'County', 'Phone', 'Mon-Fri','Mon-FI', 'Tuesday', 'Wednesday', 'Thursday', 'Sat', 'Sun', 'Latitude', 'Longitude', 'StationID']

    with open('garda_station_addresses.csv', 'w', encoding='UTF8', newline='') as garda_station_dataset:
        writer = csv.DictWriter(garda_station_dataset, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(schoolRows)



if __name__ == "__main__":
    output_json = convert_html_to_json()
    all_garda_stations = parse_json_html_tree(output_json)
    write_dict_to_csv(all_garda_stations)