import csv
from bs4 import BeautifulSoup
#import folium
import os
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

reader = csv.reader(open('google_cafe_dataset.csv','r'), delimiter = ",")

for line in reader:
    print(line[0])
#    print(line[2])
    a = line[2]
    b = a.replace("서초구", "Seocho-gu")
    c = b.split('  ')
    print(c)
