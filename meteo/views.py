from django.http import HttpResponse
from django.shortcuts import render
import geocoder
import requests
import datetime
from meteo.models import Worldcities

# Create your views here.
from django.template import loader


def temp_here(request):
    my_location = geocoder.ip('me').current_result
    location = my_location.latlng
    city = my_location.city
    country = my_location.country
    temp, cloud_cover = get_temp(location)

    context = {
        'city': city,
        'country': country,
        'temp': temp,
        'cloud_cover': cloud_cover,
    }

    return render(request, template_name='meteo/index.html', context=context)


def temp_somewhere(request):
    random_item = Worldcities.objects.order_by('?').first()
    location = [random_item.lat, random_item.lng]
    city = random_item.city
    country = random_item.country

    temp, cloud_cover = get_temp(location)

    context = {
        'city': city,
        'country': country,
        'temp': temp,
        "cloud_cover": cloud_cover,
    }

    return render(request, 'meteo/index.html', context)


def get_temp(location):
    lat, lng = location
    url = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{url}?latitude={lat}&longitude={lng}&" \
                  f"hourly=temperature_2m&hourly=cloud_cover"

    response = requests.get(api_request).json()
    hourly = response['hourly']

    now = datetime.datetime.now()
    hour = now.hour
    temp = hourly['temperature_2m'][hour]
    cloud_cover = hourly["cloud_cover"][hour]
    return temp, cloud_cover
