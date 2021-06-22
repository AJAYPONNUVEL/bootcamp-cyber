import requests
#import os
from datetime import datetime

api_key = 'a9e2f34967d0f8a862a28f6e287962d8'
location = input("enter the city name: ")
complete_api_link ="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 282.55)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d  %b  %Y  |  %I:%M:%S  %p")

print("-----------------------------------------------------------------")
print("weather status foe - {}  ||  {}".format(location.upper(),date_time))
print("-----------------------------------------------------------------")

print("Current temperature is: {:.2f'} deg C".format_map(temp_city))
print("Current weather desc   :",weather_desc)
print("Current humidity       :",hmdt, '%')
print("Current wind speed     :",wind_spd,'kmph')