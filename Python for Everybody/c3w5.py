import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


serviceurl = input('Enter XML url -')
link = urllib.request.urlopen(serviceurl)
d = link.read()
t = ET.fromstring(d)

total=0
for result in t.findall('.//count'):
    total+=int(result.text)

print(total)
