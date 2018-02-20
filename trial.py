import urllib.request
from types import MappingProxyType
import os
import sys
import json

client_id = "X8aRfxepCgSVyp81C9Jr"
clinet_secret = "oh9Jgm8XUA"
encText = urllib.parse.quote("카페","cafe")
url = "https://openapi.naver.com/v1/search/local?&query=" + encText + "&display=100&sort=comment"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", clinet_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
g = open("cafe.txt", 'w')
if (rescode==200):
	response_body = response.read()
	rt = response_body.decode('utf-8')
	new = json.loads(rt)
	info = new['items']
#	print(info)
# mapy mapx title telephone load as ordered
	b = ""
	for k in info:
		b += str(k)
	print(b)
	g.write(b)
else:
	print("Error Code:"+rescode)
g.close()
#json_rt = response.read().decode('utf-8')
#py_rt = json.loads(json_rt)
