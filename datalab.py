
#========================================
#datalab

import urllib.request
import os
import sys
import json

client_id = "X8aRfxepCgSVyp81C9Jr"
client_secret = "oh9Jgm8XUA"
url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2017-10-01\",\"endDate\":\"2018-01-01\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"비트코인\",\"keywords\":[\"비트코인\",\"bitcoin\"]},{\"groupName\":\"이더리움\",\"keywords\":[\"이더리움\",\"Ethereum\"]}],\",\"ages\":[\"1\",\"2\",\"3\",\"4\",\"5\"],}";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)