import requests
from config import API_KEY

def get_weather_data(loc):
  url = f'https://api.openweathermap.org/data/2.5/weather?q={loc}&appid={API_KEY}&units=imperial'
  
  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return None
