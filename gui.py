import tkinter as tk
from tkinter import ttk
from main import get_weather_data

class WeatherWindow(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.title('Weather Data')
        self.geometry('300x200+50+120')
        
        self.location_label = ttk.Label(self, text='', style='LocationLabel.TLabel')
        self.location_label.pack()

        self.temp_label = ttk.Label(self, text='', style='TemperatureLabel.TLabel')
        self.temp_label.pack()

        self.humidity_label = ttk.Label(self, text='', style='HumidityLabel.TLabel')
        self.humidity_label.pack()

        self.wind_label = ttk.Label(self, text='', style='WindLabel.TLabel')
        self.wind_label.pack()
        
    def update_data(self, loc, temp, humid, wind_speed):
        self.location_label.config(text=f'Location: {loc}')
        self.temp_label.config(text=f'Temperature: {temp} °F')
        self.humidity_label.config(text=f'Humidity: {humid} %')
        self.wind_label.config(text=f'Wind Speed: {wind_speed} m/h')

def display_data():
    loc = entry.get()
    data = get_weather_data(loc)

    if data:
        temp = data['main']['temp']
        humid = data['main']['humidity']
        wind_speed = data['wind']['speed']

        if not hasattr(window, 'weather_window'):
            window.weather_window = WeatherWindow(window)
            style_data()

        window.weather_window.update_data(loc, temp, humid, wind_speed)
    else:
        print("Error fetching weather data")

def style_data():
    style = ttk.Style()
    
    style.configure('LocationLabel.TLabel', font=('Arial', 15), foreground='red')
    style.configure('TemperatureLabel.TLabel', font=('Arial', 15), foreground='green')
    style.configure('HumidityLabel.TLabel', font=('Arial', 15), foreground='green')
    style.configure('WindLabel.TLabel', font=('Arial', 15), foreground='green')

window = tk.Tk()
window.title('Weather App')
window.geometry('300x200+30+50')

location = tk.StringVar()

entry = tk.Entry(window, textvariable=location)
entry.pack()

button = tk.Button(window, text='Get Weather', command=display_data)
button.pack()

refresh_bttn = tk.Button(window, text='Refresh', command=display_data)
refresh_bttn.pack()

exit_bttn = tk.Button(window, text="Exit", command=window.quit)
exit_bttn.pack()

window.mainloop()