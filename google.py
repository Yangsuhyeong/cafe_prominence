import urllib.request
import os
import sys
import json
#from googleplaces import GooglePlaces, types, lang

API_KEY = "AIzaSyCPrWFxTwfbV1LJSMPyEnroNh_Ezb2KEhI"
clinet_secret = "oh9Jgm8XUA"
encText = (37.559541, 126.943711)
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=37.559541, 126.943711&radius=500&type=restaurant&rankyby=prominence&key=" + api_key
request = urllib.request.Request(url)
#request.add_header("X-Naver-Client-Id", client_id)
#request.add_header("X-Naver-Client-Secret", clinet_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if (rescode==200):
	response_body = response.read()
	rt = response_body.decode('utf-8')
	title2 = eval(rt)
	new = json.dumps(rt)
	print(rt)
else:
	print("Error Code:"+rescode)
#json_rt = response.read().decode('utf-8')
#py_rt = json.loads(json_rt)
