# using the Uber API V1 w python
# todo:
# add exception handling
# combine uber estimates timing with google maps navigation
# kevinatgis 2016

import requests
import json
from pprint import pprint

# keys
server_token 	= '' # https://developer.uber.com/docs/rides/getting-started
headers 		= {'Authorization': 'Token {}'.format(server_token)}
url 			= 'https://api.uber.com/v1/'

# time estimate to get all available Uber Products, format: json output or print (debug)
def time_estimates(lat,lon,p_id='',format='json'):
	# https://developer.uber.com/docs/rides/api/v1-estimates-time
	if (p_id==''):
		products = requests.get(url+'estimates/time?start_latitude={}&start_longitude={}'.format(lat,lon), headers=headers)
	else:
		products = requests.get(url+'estimates/time?start_latitude={}&start_longitude={}&product_id={}'.format(lat,lon,p_id), headers=headers)

	# turns the request obj to a dict
	products_json = products.json()

	# if none available, json defaults: {'times': []} 
	if format=='json':
		if len(products_json['times']) == 0:
			return None
		else:
			return products_json['times']
	elif format=='print':
		# pretty print the json
		pprint(products_json, indent=4)

# products @ Union Station, TO
time_estimates(43.645143,-79.380655,format='print')



