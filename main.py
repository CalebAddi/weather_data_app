import requests
from config import API_KEY

def get_weather_data(city, state_or_country=None):
  loc_query = f"{city},{state_or_country}" if state_or_country else city
  coord_url = f'https://api.openweathermap.org/data/2.5/weather?q={loc_query}&appid={API_KEY}'
  
  try:
    response = requests.get(coord_url)
    response.raise_for_status()
    coord_data = response.json()
    lat, lon = coord_data['coord']['lat'], coord_data['coord']['lon']
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None

  url = f'https://api.openweathermap.org/data/2.5/weather?q={loc_query}&appid={API_KEY}&units=imperial'
  
  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None
