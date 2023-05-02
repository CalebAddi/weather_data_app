# This is the original code which you can run as a standalone python gui

import pytz
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from PIL import ImageTk, Image
from weather_app_data.weather_app.api import get_weather_data

class WeatherWindow(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.title('Weather Data')
        self.geometry('450x350+50+120')
        self.configure(bg="#303030")
        
        self.location_label = ttk.Label(self, text='', style='LocationLabel.TLabel')
        self.location_label.pack(pady=7)

        self.rain_label = ttk.Label(self, text='', style='WeatherLabel.TLabel')
        self.rain_label.pack(pady=5)

        self.temp_label = ttk.Label(self, text='', style='TemperatureLabel.TLabel')
        self.temp_label.pack(pady=5)

        self.humidity_label = ttk.Label(self, text='', style='HumidityLabel.TLabel')
        self.humidity_label.pack(pady=5)

        self.wind_label = ttk.Label(self, text='', style='WindLabel.TLabel')
        self.wind_label.pack(pady=5)

        self.wind_deg_label = ttk.Label(self, text='', style='WindDirectionLabel.TLabel')
        self.wind_deg_label.pack(pady=5)

        self.pressure_label = ttk.Label(self, text='', style='PressureLabel.TLabel')
        self.pressure_label.pack(pady=5)

        self.sunrise_label = ttk.Label(self, text='', style='SunriseLabel.TLabel')
        self.sunrise_label.pack(pady=5)

        self.sunset_label = ttk.Label(self, text='', style='SunsetLabel.TLabel')
        self.sunset_label.pack(pady=5)

    def update_data(self, loc, temp, humid, wind_speed, wind_deg, air_pressure, weather_desc, sunrise, sunset, timezone_offset):
        temp = round(temp, 1)
        humid = round(humid, 1)
        wind_speed = round(wind_speed, 1)

        self.location_label.config(text=f'Location: {", ".join(loc)}')
        self.temp_label.config(text=f'Temperature: {temp} °F')
        self.humidity_label.config(text=f'Humidity: {humid} %')
        self.wind_label.config(text=f'Wind Speed: {wind_speed} mph')
        self.wind_deg_label.config(text=f'Wind Direction: {wind_deg}°')
        self.pressure_label.config(text=f'Air Pressure: {air_pressure} hPa')
        self.rain_label.config(text=f'Weather: {weather_desc}')

        # converting UNIX timestamp to readable time
        timezone = pytz.FixedOffset(timezone_offset / 60)
        sunrise_time = datetime.fromtimestamp(sunrise, timezone).strftime('%I:%M %p')
        sunrise_time = sunrise_time[:-2] + 'AM' # Hard coded to prevent it from showing as PM for some reason
        sunset_time = datetime.fromtimestamp(sunset, timezone).strftime('%I:%M:%S %p')

        self.sunrise_label.config(text=f'Sunrise: {sunrise_time}')
        self.sunset_label.config(text=f'Sunset: {sunset_time}')

def display_data():
    loc = entry.get().split(',')
    city = loc[0].strip()
    state_or_country = loc[1].strip() if len(loc) > 1 else None
    data = get_weather_data(city, state_or_country)
    # print(data)

    if data:
        temp = data['main']['temp']
        humid = data['main']['humidity']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        air_pressure = data['main']['pressure']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        timezone_offset = data['timezone']

        # check the current weather
        weather_desc = ''
        if 'weather' in data:
            weather_desc = data['weather'][0]['description'].upper()

        if not hasattr(window, 'weather_window'):
            window.weather_window = WeatherWindow(window)
            style_data()

        window.weather_window.update_data(loc, temp, humid, wind_speed, wind_deg, air_pressure, weather_desc, sunrise, sunset, timezone_offset)
    else:
        print("Error fetching weather data")

def style_data():
    style = ttk.Style()
    style.configure('TLabel', background='#303030')
    
    style.configure('LocationLabel.TLabel', font=('Arial', 20, 'bold'), foreground='#F08080')
    style.configure('WeatherLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#B0E0E6')
    style.configure('TemperatureLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#BDFCC9')
    style.configure('HumidityLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#BDFCC9')
    style.configure('WindLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#98FB98')
    style.configure('WindDirectionLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#98FB98')
    style.configure('PressureLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#D1D1E0')
    style.configure('SunriseLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#FFE4E1')
    style.configure('SunsetLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#FFE4E1')

window = tk.Tk()
window.title('Weather App')
window.geometry('320x220+30+50')
window.configure(bg='#303030')

location = tk.StringVar()

entry = tk.Entry(window, textvariable=location, font=('Times New Roman', 20), width=20)
entry.pack(pady=20, padx=20)

button = tk.Button(window, text='Get Weather', command=display_data, font=('Times New Roman', 18), bg='#3a3a3a')
button.pack(pady=5, padx=15)

refresh_bttn = tk.Button(window, text='Refresh', command=display_data, font=('Times New Roman', 18), bg='#3a3a3a')
refresh_bttn.pack(pady=5, padx=15)

exit_bttn = tk.Button(window, text="Exit", command=window.quit, font=('Times New Roman', 18), bg='#3a3a3a')
exit_bttn.pack(pady=5, padx=15)

window.mainloop()