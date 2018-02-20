import urllib
import os
import sys
import json

import googleplaces
from googleplaces import GooglePlaces, types, lang
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

MAX_FETCH = 200
AUTH_KEY = "AIzaSyCPrWFxTwfbV1LJSMPyEnroNh_Ezb2KEhI"

#url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?&key=" + AUTH_KEY + "&location"
google_places = GooglePlaces(AUTH_KEY)
#google_places = GooglePlaces(AUTH_KEY)
query_result = google_places.nearby_search(
	location = 'Seoul, Korea', keyword = 'cafe', rankby = 'prominence', type = 'cafe', radius = 50000)
#text_search API
if query_result.has_attributions :
	print(query_result.html_attributions)

fetched = 0
dataset2 = open("google_cafes.txt", 'w')
download_dir = "google_cafe_dataset.csv"

dataset = open(download_dir, 'w')
columTitleRows = "name, rating, vicinity, lat, lng\n"
dataset.write(columTitleRows)

while fetched < MAX_FETCH :
	for place in query_result.places:
		name = place.name
		place.get_details()
		rating = str(place.rating)
		vic = str(place.details['vicinity'])
		vic2 = vic.replace(","," ")
		lat = str(place.details['geometry']['location']['lat'])
		lng = str(place.details['geometry']['location']['lng'])
#		print('[%i] %s'%(fetched, name))
#		print(rating)
		print(vic2)
#		print(lat)
#		print(lng)
		fetched = fetched + 1
		row = name + "," + rating + "," + vic2 + "," + lat + "," + lng + "\n"
		dataset2.write(row)
		dataset.write(row)
	if query_result.has_next_page_token:
		print('=========================================')
		print('[NPT: %s]'%(query_result.next_page_token))
		print('=========================================')
		query_result = google_places.nearby_search(
			pagetoken = query_result.next_page_token)
#		row = name + "," + rating + "," + vic + "," + lat + "," + lng + "\n"
#		dataset2.write(row)

#for place in query_result.places:
#	print(place.name)
#	print(place.geo_location)
#	print(place.place_id)
#	place.get_details()
#	print(place.details)
#	print(place.url) #local_phone_number, website,

#for photo in place.photos :
#	photo.get(maxheight=500, maxwidth=500)
#	photo.mimetype
#	photo.url
#	photo.filename
#	photo.data

#additional pages of results?
#if query_result.has_next_page_token:
#	query_result_next_page = google_places.nearby_search(
#		pagetoken = query_result.next_page_token)
