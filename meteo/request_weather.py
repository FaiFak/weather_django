import geocoder
import requests
import datetime


def temp_here():
    location = geocoder.ip('me').current_result.latlng
    latitude, longitude = location

    url = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{url}?latitude={latitude}&longitude={longitude}&" \
                  f"hourly=temperature_2m"

    response = requests.get(api_request).json()

    now = datetime.datetime.now()
    hour = now.hour
    temp = response['hourly']['temperature_2m'][hour]

    return temp

print(temp_here())