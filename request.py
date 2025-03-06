import time
import xml.etree.ElementTree as ET
import requests

while True:
    r = requests.get("https://boardgamegeek.com/xmlapi2/collection?username=Dynzad&excludesubtype=boardgameexpansion")
    status = r.status_code
    print(status)
    if status != 202:
        break
    time.sleep(3)


root = ET.fromstring(r.text)
for element in root:
    item = element.find('name').text
    object_id = element.attrib['objectid']
    print (str(object_id) + ': ' + item)
