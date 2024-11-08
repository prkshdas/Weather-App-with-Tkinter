import requests
from tkinter import Tk, Label, Entry, Button

def get_weather():
    city = city_entry.get()
    api_key = "535c94ae3baa820cadf9549dcb50dbc3"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            temp = main["temp"]
            feels_like = main["feels_like"]
            description = weather["description"]

            result_label.config(text=f"Weather in {city.capitalize()}:\n"
                                     f"Temperature: {temp}°C\n"
                                     f"Feels Like: {feels_like}°C\n"
                                     f"Description: {description.capitalize()}")
        else:
            result_label.config(text=f"City '{city}' not found. Please check the spelling.")
    except Exception as e:
        result_label.config(text="Error occurred: Unable to retrieve data")

# GUI setup
root = Tk()
root.title("Weather App")
root.geometry("400x300")

# City Label and Entry
city_label = Label(root, text="Enter city name:", font=("Arial", 14))
city_label.pack(pady=10)
city_entry = Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

# Get Weather Button
get_weather_button = Button(root, text="Get Weather", command=get_weather, font=("Arial", 14))
get_weather_button.pack(pady=10)

# Result Label
result_label = Label(root, text="", font=("Arial", 14), justify="left")
result_label.pack(pady=10)

root.mainloop()
