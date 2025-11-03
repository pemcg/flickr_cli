# f/5.6ish

import requests
import urllib.parse
import keys
import sys

HERE_URL = 'https://geocode.search.hereapi.com/v1/geocode'

# -------------------- Here API Methods ------------------
# --------------------------------------------------------

def get_geo_coordinates_from_location(location):

    # Example location: "Winchester cathedral" or "Southampton"

    headers = {'accept': 'application/json', "Content-Type": "application/json"}
    data = {
        'apiKey': keys.HERE_API_KEY,
        'in': 'countryCode:GBR'
    }
    data['q'] = urllib.parse.quote_plus(location)

    try:
        response = requests.get(HERE_URL, headers=headers, params=data)
        response.raise_for_status()
        lat = response.json()['items'][0]['position']['lat']
        lon = response.json()['items'][0]['position']['lng']
        return {'lat': lat, 'lon': lon}
    except requests.exceptions.HTTPError as ex:
        print('HereError:', ex)
        sys.exit()

# ----------------- End of Here API Methods --------------
# --------------------------------------------------------