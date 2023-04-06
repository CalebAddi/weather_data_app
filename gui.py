import tkinter as tk
from tkinter import ttk
from main import get_weather_data

def display_data():
    loc = entry.get()
    data = get_weather_data(loc)
    temp = data['main']['temp']
    humid = data['main']['humidity']
    wind_speed = data['wind']['speed']

    if not hasattr(window, 'weather_window'):
        window.weather_window = tk.Toplevel(window)
        window.weather_window.title('Weather Data')
        window.weather_window.geometry('300x200+50+120')
        
        location_label = ttk.Label(window.weather_window, text=f'Location: {loc}', style='LocationLabel.TLabel')
        location_label.pack()

        temp_label = ttk.Label(window.weather_window, text=f'Temperature: {temp} °F', style='TemperatureLabel.TLabel')
        temp_label.pack()

        humidity_label = ttk.Label(window.weather_window, text=f'Humidity: {humid} %', style='HumidityLabel.TLabel')
        humidity_label.pack()

        wind_label = ttk.Label(window.weather_window, text=f'Wind Speed: {wind_speed} m/h', style='WindLabel.TLabel')
        wind_label.pack()
    else:
        window.weather_window.children['!label'].config(text=f'Location: {loc}')
        window.weather_window.children['!label2'].config(text=f'Temperature: {temp} °F')
        window.weather_window.children['!label3'].config(text=f'Humidity: {humid} %')
        window.weather_window.children['!label4'].config(text=f'Wind Speed: {wind_speed} m/h')

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

button = tk.Button(window, text='Get Weather', command=lambda: [display_data(), style_data()])
button.pack()

window.mainloop()