import urllib, json
import googlemap

def GoogPlac(lat, lng, types, key):
	AUTH_KEY = key
	LOCATION = str(lat) + "," + str(lng)
	RADIUS = radius
	TYPES = types
	MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&types=%s'
           '&sensor=false&key=%s') % (LOCATION, TYPES, AUTH_KEY)
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
MyKey = 'AIzaSyD594CyJiZ1Do5W81QozG4k16YhJe3sduk'
MyType = 'cafe'

for m in range(0,100):
	search = GoogPlac(lat=d[m]['mapy'], lng = d[m]['mapx'], types=MyType, key = MyKey)
#	if search['status'] == 'ok' :
#		for place in search['results']:
#			x = IterJson(place)
#			results = list(case) + x
