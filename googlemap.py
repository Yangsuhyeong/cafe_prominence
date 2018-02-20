import urllib, json
import googleplaces
from googleplaces import GooglePlaces, types, lang

def GoogPlac(lat, lng, radius,type, key):
	AUTH_KEY = key
	LOCATION = str(lat) + "," + str(lng)
	RADIUS = radius
	TYPE = type
	MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&type=%s'
           '&sensor=false&key=%s') % (LOCATION, RADIUS, TYPE, AUTH_KEY)
#grabbing the Json result
	response = urllib.urlopen(MyUrl)
	jsonRaw = response.read()
	jsonData = json.loads(jsonRaw)
	return jsonData

#helper to grab the Json data that I want in a list
def IterJson(place):
	x = [place['name'], place['reference'], place['geometry']['location']['lat'],
	place['geometry']['location']['lng'], place['vicinity']]
	return x

#setting the parameters I use in the query = type and my key
MyKey = 'AIzaSyCPrWFxTwfbV1LJSMPyEnroNh_Ezb2KEhI'
MyType = 'cafe'
