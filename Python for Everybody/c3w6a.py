import json
import urllib.request

url=input('Enter url-')
d=urllib.request.urlopen(url)
jdata=json.load(d)
total=0
for info in jdata['comments']:
    print(info['count'])
    total+=info['count']
print(total)
