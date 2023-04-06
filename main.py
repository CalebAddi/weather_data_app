import requests

def get_weather_data(loc):
  api_key = '04c0aca76b4ff4a68b98fe58d29c9e1a'
  url = f'https://api.openweathermap.org/data/2.5/weather?q={loc}&appid={api_key}&units=imperial'
  response = requests.get(url)
  data = response.json()
  return data
