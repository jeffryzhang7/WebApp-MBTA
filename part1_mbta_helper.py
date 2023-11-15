### 1. Accessing Web Data Programmatically
import requests

def get_coordinates(place_name, access_token):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json?access_token={access_token}"
    response = requests.get(url)
    data = response.json()
    
    if 'features' in data and len(data['features']) > 0:
        longitude, latitude = data['features'][0]['center']
        return latitude, longitude
    else:
        print("No coordinates found for the specified place.")
        return None

# place_name = "Boston Common"
# access_token = "pk.eyJ1IjoiamVmZnJ5emhhbmciLCJhIjoiY2xveXA4cDBoMDViZDJqbzUxd2xsMzB1MiJ9.KNQqcz1W-NEqGyLC6nhYsA"
# coordinates = get_coordinates(place_name, access_token)
# print(coordinates)  

### 2. Structured Data Responses (JSON)
import json
import pprint
import urllib.request

MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MAPBOX_TOKEN = 'pk.eyJ1IjoiamVmZnJ5emhhbmciLCJhIjoiY2xveXA4cDBoMDViZDJqbzUxd2xsMzB1MiJ9.KNQqcz1W-NEqGyLC6nhYsA'
query = 'Boston Common'
query = query.replace(' ', '%20') 
url=f'{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi'
print(url) 


# print(response_data['features'][0]['properties']['address'])


def extract_coordinates(json_response):
    """
    Extracts latitude and longitude from a Mapbox API JSON response
    and return A tuple (latitude, longitude) if coordinates are found, otherwise None.
    """
    if 'features' in json_response and len(json_response['features']) > 0:
        longitude, latitude = json_response['features'][0]['center']
        return latitude, longitude
    else:
        print("No coordinates found in the JSON response.")
        return None

json_response_example = {
    "features": [
        {
            "center": [-71.069351, 42.35725],
        },
    ],
}

coordinates = extract_coordinates(json_response_example)
# print(coordinates)


### 4. Getting Local
import urllib.request
import urllib.parse

def find_closest_mbta_stop(latitude, longitude, api_key):
    base_url = "https://api-v3.mbta.com/stops"
    params = {
        'sort': 'distance',
        'filter[latitude]': latitude,
        'filter[longitude]': longitude,
        'api_key': api_key
    }

    query_string = urllib.parse.urlencode(params)
    url = f"{base_url}?{query_string}"

    try:
        with urllib.request.urlopen(url) as response:
            response_data = json.loads(response.read())
            if response_data['data'] and len(response_data['data']) > 0:
                closest_stop = response_data['data'][0]
                stop_name = closest_stop['attributes']['name']
                wheelchair_accessible = closest_stop['attributes']['wheelchair_boarding']
                return stop_name, "Yes" if wheelchair_accessible == 1 else "No"
            else:
                return "No stops found", "N/A"
    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None

# Testing
# api_key = "f1b5807a6651432ea9b82af220367e1a"  
# latitude, longitude = 42.35725, -71.069351  
# closest_stop, is_accessible = find_closest_mbta_stop(latitude, longitude, api_key)
# print("Closest Stop:", closest_stop, "| Wheelchair Accessible:", is_accessible)


# 5. To wrap up
import json
import urllib.request
import urllib.parse

def combined_tool(place_name, mapbox_access_token, mbta_api_key):
    def get_coordinates(place_name):
        encoded_place_name = urllib.parse.quote(place_name)
        url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{encoded_place_name}.json?access_token={mapbox_access_token}"

        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode())
                if 'features' in data and len(data['features']) > 0:
                    longitude, latitude = data['features'][0]['center']
                    return latitude, longitude
                else:
                    return None, None
        except Exception as e:
            print(f"Error occurred: {e}")
            return None, None

    def find_closest_mbta_stop(latitude, longitude):
        base_url = "https://api-v3.mbta.com/stops"
        params = {
            'sort': 'distance',
            'filter[latitude]': latitude,
            'filter[longitude]': longitude,
            'api_key': mbta_api_key
        }

        query_string = urllib.parse.urlencode(params)
        url = f"{base_url}?{query_string}"

        try:
            with urllib.request.urlopen(url) as response:
                response_data = json.loads(response.read().decode())
                if response_data['data'] and len(response_data['data']) > 0:
                    closest_stop = response_data['data'][0]
                    stop_name = closest_stop['attributes']['name']
                    wheelchair_accessible = closest_stop['attributes']['wheelchair_boarding']
                    return stop_name, "Yes" if wheelchair_accessible == 1 else "No"
                else:
                    return "No stops found", "N/A"
        except Exception as e:
            print(f"Error occurred: {e}")
            return None, None

    latitude, longitude = get_coordinates(place_name)
    if latitude is None or longitude is None:
        return "Could not find coordinates."

    closest_stop, is_accessible = find_closest_mbta_stop(latitude, longitude)
    return f"Closest MBTA Stop: {closest_stop}, Wheelchair Accessible: {is_accessible}"

# Example Usage
place_name = "Quincy"
mapbox_access_token = "pk.eyJ1IjoiamVmZnJ5emhhbmciLCJhIjoiY2xveXA4cDBoMDViZDJqbzUxd2xsMzB1MiJ9.KNQqcz1W-NEqGyLC6nhYsA"
mbta_api_key = "f1b5807a6651432ea9b82af220367e1a"
result = combined_tool(place_name, mapbox_access_token, mbta_api_key)
print(result)
