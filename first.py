from config import config
import requests, json

API_KEY = config.weather_api_key.get_secret_value()

def get_coordinates(city: str):
    result = requests.get(url=f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}')
    coordinates = None
    if result.status_code == 200:
        data = result.json()[0]
        coordinates = {
            "lat": data['lat'],
            "lon": data['lon'],
        }
    return coordinates

city = input('Enter city name: ')
coordinates = get_coordinates(city)
if coordinates:
    link = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates['lat']}&lon={coordinates['lon']}&appid={API_KEY}"
    result = requests.get(
        url = link,
        timeout=2
    )
    if result.status_code == 200:
        data = result.json()
        print(data)
    else:
        print('Something went wrong')
else:
    print('Nothing was found :(')
