from bs4 import BeautifulSoup
import requests
import time
from time import gmtime, strftime
from plyer import notification

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

print('zadaj mesto')
city = input(str())

print('zadaj frekvenciu hlásenia (minúty)')
x = int(input())


def mintosec():
    i = x * 60
    return i


def weather(city):
    global res
    try:
        city = city.replace(" ", "+")
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers)
    except ValueError or RuntimeError:
        print('check your internet connection')

    while headers:
        print(strftime("%d-%m %H:%M:%S", gmtime()))
        soup = BeautifulSoup(res.text, 'html.parser')

        location = soup.select('#wob_loc')[0].getText().strip()
        current_time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()

        information = f"{location}\n{current_time}\n{info}\n{weather} °C "
        print(information)
        notification.notify(
            app_name='WeatherApp',
            title='Počasie' + strftime("%d-%m %H:%M:%S", gmtime()),
            message=information,
            timeout=int(5)
        )

        time.sleep(mintosec())


city = city + " weather"
weather(city)
