import requests
from pprint import pprint
import time
from time import gmtime, strftime

# API settings
API_KEY = 'dbc83d83a2892871b4afdaa3cf4b50af'
unites = 'metric'
lang = 'sk'


print('zadaj mesto')


# city function
def city():
    city = input(str())
    if city == str('sered'):
        city = str('galanta')
    else:
        city = city
    return str(city)


# link creation
baseurl = 'http://api.openweathermap.org/data/2.5/weather?q=' + city() + '&units=' + unites + '&appid=' + API_KEY

# user selected report frequency
print('set report frequency (minutes)')
x = int(input())


def mintosec():
    i = x * 60
    return i


# weather report loop
while baseurl:
    print(strftime("%d-%m %H:%M:%S", gmtime()))
    weather_data = requests.get(baseurl).json()
    pprint(weather_data)
    time.sleep(mintosec())
