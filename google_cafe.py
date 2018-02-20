import urllib
import os
import sys
import json
import googleplaces
from googleplaces import GooglePlaces, types, lang
AUTH_KEY = "AIzaSyCPrWFxTwfbV1LJSMPyEnroNh_Ezb2KEhI"

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?&key=" + AUTH_KEY + "&location"
google_places = GooglePlaces(AUTH_KEY)
#google_places = GooglePlaces(AUTH_KEY)
query_result = google_places.nearby_search(
	location = 'Seoul, Korea', keyword = 'cafe', rankby = 'prominence', type = 'cafe', radius = 50000)
#text_search API
if query_result.has_attributions :
	print(query_result.html_attributions)

for place in query_result.places:
	print(place.name)
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
if query_result.has_next_page_token:
	query_result_next_page = google_places.nearby_search(
		pagetoken = query_result.next_page_token)

