#import
import requests
from pprint import pprint
import time
#API
API_KEY = 'dbc83d83a2892871b4afdaa3cf4b50af'

print('zadaj mesto')

#city function
def city():
    city = input(str())
    if city == str('vrbove') or city == str('sered'):
        city = str('bratislava')
    else:
        city = city
    return str(city)

#link creation
unites = 'metric'
lang = 'sk'
baseurl = 'http://api.openweathermap.org/data/2.5/weather?q=' + city() + '&units=' + unites + '&appid=' + API_KEY

print(baseurl)

i = True
#loop
while i:
    weather_data = requests.get(baseurl).json()
    pprint(weather_data)
    print('do ya want to have weather report every 10min, write y or n ?')
    input(str())
    if input() == str('y'):
        time.sleep(1)
    continue
