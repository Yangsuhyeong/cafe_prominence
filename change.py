import googleplaces
from googleplaces import GooglePlaces, types, lang

AUTH_KEY = "AIzaSyCPrWFxTwfbV1LJSMPyEnroNh_Ezb2KEhI"

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?&key=" + AUTH_KEY + "&location"
google_places = GooglePlaces(AUTH_KEY)
#google_places = GooglePlaces(AUTH_KEY)
query_result = google_places.radar_search(
	location = 'Seoul, Korea', radius = 50000, keyword = 'cafe', type = 'cafe')

if query_result.has_attributions : 
	print(query_result.html_attributions)

print(query_result.place_id)
#for place in query_result.place_id:
#	print(place.geo_location)
#	print(place.place_id)
#	place.get_details()
#	print(place.details)
#	print(place.url) #local_phone_number, website, 
