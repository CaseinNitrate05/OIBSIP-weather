import datetime as dt
import requests

BASE_URL="http://api.openweathermap.org/data/2.5/weather?"
API_KEY="442cac6e57e6361e9850e284a1a5eeea"
CITY=input("Enter the city name:")


def K_to_C_F(kelvin):
    celsius=kelvin-273.15
    fahrenheit=celsius*(9/5)+32
    return celsius,fahrenheit


url=BASE_URL+"appid="+API_KEY+"&q="+CITY

response=requests.get(url).json()

temp_kelvin=response['main']['temp']
temp_celsius,temp_fahrenheit=K_to_C_F(temp_kelvin)

feels_like_kelvin=response['main']['feels_like']
feels_like_celsius,feels_like_fahrenheit=K_to_C_F(feels_like_kelvin)

wind_speed=response['wind']['speed']
humidity=response['main']['humidity']
description=response['weather'][0]['description']

sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

print("In"+" "+CITY)
print(f"Temperature : {temp_celsius:.2f}C or {temp_fahrenheit:.2f}F")
print(f"Feels like: {feels_like_celsius:.2f}C or {feels_like_fahrenheit:.2f}F")
print(f"Humidity : {humidity}%")
print(f"Wind Spped : {wind_speed}m/s")
print(f"General Weather : {description}")
print(f"Sunrise : {sunrise_time}")
print(f"Sunset : {sunset_time}")
