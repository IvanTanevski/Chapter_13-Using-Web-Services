# Exercise 1: Change either the www.py4e.com/code3/geojson.py or www.py4e.com/code3/geoxml.py to print out 
# the two-character country code from the retrieved data. Add error checking so your program does not traceback 
# if the country code is not there. Once you have it working, search for "Atlantic Ocean" and make sure 
# it can handle locations that are not in any country.

# Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle Locations 3295-3299). Kindle Edition. 

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)                             # Creating JSON format, or empty object to avoid traceback
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue                                          # If empty object, or status not OK, running again the loop

    print(json.dumps(js, indent=4))

    location = js['results'][0]                 # Creating location list by accesing results[0] location in the json object
    add_comp = location['address_components']   # Creating add_comp list with all 'address_component' tags within location
    country = False
    
    for add in add_comp:                        # Iterating through add_comp list, creating types variable which is the value
        types = add['types']                    # of every 'types' key in address_components. When the program finds the 
        if types == ['country', 'political']:   # required values (country and political) prints the country code (short_name)
            country = True
            print(add["short_name"])
    
    if country != True:
        print('No one\'s land')                 # If not country found (like Atlantic ocean example) prints No one's land
