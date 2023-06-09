import pytz
from django.shortcuts import render
from django.http import JsonResponse
from .models import WeatherData
from .api import get_weather_data
from datetime import datetime, timedelta
from timezonefinder import TimezoneFinder


def fetch_weather(request):
    city = request.GET.get('city')
    state_or_country = request.GET.get('state_or_country')

    if not city:
        return JsonResponse({'status': 'error', 'message': 'City is required'})

    data = get_weather_data(city, state_or_country)

    if data:
        lat, lon = data['coord']['lat'], data['coord']['lon']
        timefind = TimezoneFinder()
        tzName = timefind.timezone_at(lat = lat, lng = lon)
        local_tz = pytz.timezone(tzName) if tzName else pytz.UTC

        sunrise_utc = datetime.utcfromtimestamp(data['sys']['sunrise'])
        sunset_utc = datetime.utcfromtimestamp(data['sys']['sunset'])
        sunrise_utc = datetime.utcfromtimestamp(data['sys']['sunrise'])
        sunset_utc = datetime.utcfromtimestamp(data['sys']['sunset'])

        weather_data = WeatherData.objects.create(
            city = city,
            state_or_country = state_or_country,
            temp = data['main']['temp'],
            humid = data['main']['humidity'],
            wind_speed = data['wind']['speed'],
            wind_deg = data['wind']['deg'],
            air_pressure = data['main']['pressure'],
            weather_desc = data['weather'][0]['description'].upper(),
            sunrise=sunrise_utc.strftime('%Y-%m-%d %H:%M:%S'),
            sunset=sunset_utc.strftime('%Y-%m-%d %H:%M:%S'),
        )

        # print(data)

        weather_data.save()
        response = {
            'status': 'success',
            'data': data,
        }
    else:
        response = {
            'status': 'error',
            'message': 'Error with fetching weather data',
        }

    return JsonResponse(response)