import json
import ast
import csv
import collections

f = open("cafe.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line[0:50])
f.close()

line.find('mapy')
new = open("easy.txt",'w')

a = line.replace("}{","},,{")
b = a.replace("{'mapx':", "{ 'mapx':")
s = b.split(',,')

new.write('\n'.join(s))
new.close

z = open("final.txt",'w')

for i in range(0,len(s)):
	s[i] = eval(s[i])

# mapy mapx title telephone load as ordered
d = collections.OrderedDict()
d = s

for l in range(0, 100):
	del d[l]['address']
	del d[l]['category']
	del d[l]['description']
	del d[l]['link']

z.write('\n'.join(str(v) for v in d))
z.close

download_dir = "exampleCsv.csv"

csv = open(download_dir, "w")
columTitleRows = "title, mapx, mapy, telephone, roadAddress\n"
csv.write(columTitleRows)
print(columTitleRows)

for k in range(0,100):
	title = d[k].get('title')
	mapx = d[k].get('mapx')
	mapy = d[k].get('mapy')
	telephone = d[k].get('telephone')
	roadAddress = d[k].get('roadAddress')
	row = title + "," + mapx + "," + mapy + "," + telephone + "," + roadAddress + "\n"
	csv.write(row)
#==================================================================
#geocoding
