#!/bin/python3
# names of people in space right now

import json
import urllib.request

url = 'http://api.open-notify.org/astros.json'

response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)
print('People in space: ', result['number'])
people = result['people']

for p in people:
    print(p['name'],"in",p['craft'])


