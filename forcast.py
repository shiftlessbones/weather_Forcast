import requests
import tkinter as tk
from tkinter import messagebox

# Function to get weather data
def get_weather(city):
    api_key = "your API"  # Replace with your own API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,#  key stands for "query" and is used to specify the location
        'appid': api_key,# key stands for "API ID" or "API Key"
        'units': 'metric'# parameter specifies the units of measurement for the weather data
    }
    response = requests.get(base_url, params=params)
    return response.json()

# Function to display weather data
def display_weather():
    city = city_entry.get()
    if city:
        weather_data = get_weather(city)
        if weather_data['cod'] == 200:
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            weather_info = f"Temperature: {temp}°C\nDescription: {description}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
            result_label.config(text=weather_info)
        else:
            messagebox.showerror("Error", "City not found!")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name")

# Setting up the GUI
root = tk.Tk()
root.title("Weather Forecast App")

city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=50)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=display_weather)
get_weather_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

root.mainloop()
