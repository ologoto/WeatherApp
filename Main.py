import time
from pprint import pprint
from time import gmtime, strftime
from plyer import notification

import requests

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
baseurl = 'http://api.openweathermap.org/data/2.5/weather?q=' + city() + '&units=' + unites + '&mode=' + '&appid=' + API_KEY
# baseurl1 = 'https://api.openweathermap.org/data/2.5/forecast?q=' + city() + '&units=' + unites + '&appid=' + API_KEY

print(baseurl)

# user selected report frequency
print('set report frequency (minutes)')
x = int(input())


def mintosec():
    i = x * 60
    return i


# weather report loop
while baseurl:
    print(strftime("%d-%m %H:%M:%S", gmtime()))
    try:
        weather_data = requests.get(baseurl).json()
        pprint(weather_data)
        notification.notify(
            title='weather report  ' + strftime("%d-%m %H:%M:%S", gmtime()),
            message=weather_data,
            app_name='WeatherApp',
        )
        time.sleep(mintosec())
    except RuntimeError or ValueError:
        break




