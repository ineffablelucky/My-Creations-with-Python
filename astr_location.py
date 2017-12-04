#!/bin/python3
# location of ISS now in space

import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/iss-now.json'

response = urllib.request.urlopen(url)
result = json.loads(response.read())
location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude', lat)
print('Longitude', lon)

while True:
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(float(lon), float(lat))
    input()


