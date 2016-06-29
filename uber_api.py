# using the uber API
# no need to request a ride, only to gather general information
# oauth is only used to avoid making the user give their username/pw to a third party
# kevinatgis

# combine uber estimates timing with google maps navigation

import requests

# keys
server_token = ''
headers = {'Authorization': 'Token {}'.format(server_token)}
url = 'https://api.uber.com/v1/'

# time estimate to get all available Uber Products
def time_estimates(lat,lon,p_id=''):
	# curl -H 'Authorization: Token INSERT_TOKEN_HERE' \
	# 'https://api.uber.com/v1/estimates/time?start_latitude=37.43.645143&start_longitude=-79.380655'

	if (p_id==''):
		products = requests.get(url+'estimates/time?start_latitude={}&start_longitude={}'.format(lat,lon), headers=headers)
	else:
		products = requests.get(url+'estimates/time?start_latitude={}&start_longitude={}&product_id={}'.format(lat,lon,p_id), headers=headers)

	print(products.text)

# products @ Union Station, TO
time_estimates(43.645143,-79.380655)



