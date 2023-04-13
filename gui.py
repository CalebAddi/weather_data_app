import pytz
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from PIL import ImageTk, Image
from main import get_weather_data

class WeatherWindow(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.title('Weather Data')
        self.geometry('450x350+50+120')
        
        self.location_label = ttk.Label(self, text='', style='LocationLabel.TLabel')
        self.location_label.pack(pady=7)

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

        self.rain_label = ttk.Label(self, text='', style='RainLabel.TLabel')
        self.rain_label.pack(pady=5)

    def update_data(self, loc, temp, humid, wind_speed, wind_deg, air_pressure, is_raining, sunrise, sunset, timezone_offset):
        temp = round(temp, 1)
        humid = round(humid, 1)
        wind_speed = round(wind_speed, 1)

        self.location_label.config(text=f'Location: {loc}')
        self.temp_label.config(text=f'Temperature: {temp} °F')
        self.humidity_label.config(text=f'Humidity: {humid} %')
        self.wind_label.config(text=f'Wind Speed: {wind_speed} mph')
        self.wind_deg_label.config(text=f'Wind Direction: {wind_deg}°')
        self.pressure_label.config(text=f'Air Pressure: {air_pressure} hPa')
        self.rain_label.config(text=f'Raining: {"Yes" if is_raining else "No"}')

        # converting UNIX timestamp to readable time
        timezone = pytz.FixedOffset(timezone_offset / 60)
        sunrise_time = datetime.fromtimestamp(sunrise, timezone).strftime('%I:%M %p')
        sunrise_time = sunrise_time[:-2] + 'AM' # Hard coded to prevent it from showing as PM for some reason
        sunset_time = datetime.fromtimestamp(sunset, timezone).strftime('%I:%M:%S %p')

        self.sunrise_label.config(text=f'Sunrise: {sunrise_time}')
        self.sunset_label.config(text=f'Sunset: {sunset_time}')

def display_data():
    loc = entry.get()
    data = get_weather_data(loc)
    print(data)

    if data:
        temp = data['main']['temp']
        humid = data['main']['humidity']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        air_pressure = data['main']['pressure']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        timezone_offset = data['timezone']

        # check if it is raining at the location
        is_raining = False
        if 'rain' in data and '1h' in data['rain'] and data['rain']['1h'] > 0.0:
            is_raining = True
        elif 'weather' in data:
            for weather in data['weather']:
                if 'rain' in weather['main'].lower():
                    is_raining = True
                    break


        if not hasattr(window, 'weather_window'):
            window.weather_window = WeatherWindow(window)
            style_data()

        window.weather_window.update_data(loc, temp, humid, wind_speed, wind_deg, air_pressure, sunrise, sunset, is_raining, timezone_offset)
    else:
        print("Error fetching weather data")

def style_data():
    style = ttk.Style()
    
    style.configure('LocationLabel.TLabel', font=('Arial', 20, 'bold'), foreground='#F08080')
    style.configure('TemperatureLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#BDFCC9')
    style.configure('HumidityLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#BDFCC9')
    style.configure('WindLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#98FB98')
    style.configure('WindDirectionLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#98FB98')
    style.configure('PressureLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#D1D1E0')
    style.configure('SunriseLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#FFE4E1')
    style.configure('SunsetLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#FFE4E1')
    style.configure('RainLabel.TLabel', font=('Arial', 15, 'italic'), foreground='#B0E0E6')

window = tk.Tk()
window.title('Weather App')
window.geometry('350x250+30+50')
window.configure(bg='#FFDAB9')

location = tk.StringVar()

entry = tk.Entry(window, textvariable=location, font=('Times New Roman', 16))
entry.pack(pady=30, padx=20)

button = tk.Button(window, text='Get Weather', command=display_data, font=('Times New Roman', 14), bg='#3a3a3a')
button.pack(pady=10, padx=15)

refresh_bttn = tk.Button(window, text='Refresh', command=display_data, font=('Times New Roman', 14), bg='#3a3a3a')
refresh_bttn.pack(pady=10, padx=15)

exit_bttn = tk.Button(window, text="Exit", command=window.quit, font=('Times New Roman', 14), bg='#3a3a3a')
exit_bttn.pack(pady=10, padx=15)

window.mainloop()