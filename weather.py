#!usr/bin/env python

from urllib2 import Request, urlopen, URLError

import json

city_list = ("Cambridge,USA", "Berkeley", "Oakland", "Palo_Alto")

api_key = '306e98f72c67de6deffd7ac8f6151565'


city_clean = []
temps = []

for city in city_list:
    #print city
    weather_api_call = "http://api.openweathermap.org/data/2.5/find?q="+city+"&mode=json&units=imperial&APPID="+api_key
    #print weather_api_call

    weather_call = urlopen(weather_api_call)
    weather = weather_call.read()

    data = json.loads(weather)
    #print data
    clean_city = data["list"][0]["name"]
    str(clean_city)
    print clean_city
    temp = data["list"][0]["main"]["temp"]
    print temp

    city_clean.append(clean_city)
    temps.append(temp)


temps_dict = {}

cities_and_temps = zip(city_clean, temps)
 
for city, temp in cities_and_temps:
    temps_dict[city] = temp
    
for key, value in temps_dict.iteritems() :
    happy = key + ":", value

    
