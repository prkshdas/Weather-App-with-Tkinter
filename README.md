# Weather App with Tkinter

This is a simple Weather App created using Python's tkinter library for the graphical interface and the requests library to fetch real-time weather data from the OpenWeatherMap API. This app allows users to enter a city name and retrieve the current temperature, weather description, and "feels like" temperature for that location.

## Features

City-Based Weather Lookup: Enter any city name to get the current weather details.
Graphical Interface: A clean and user-friendly interface built with tkinter.
Real-Time Data: Uses the OpenWeatherMap API to fetch real-time weather information.
Error Handling: Handles cases where the city is not found or the API call fails.

## Prerequisites

Python: Make sure Python 3 is installed on your system.
Requests Library: Install the requests library to make API calls.

```python
pip install requests
```

## How to Use

Get an API Key from OpenWeatherMap
Sign up at OpenWeatherMap to get a free API key, which is needed to access weather data.

Clone the Repository
Clone or download the repository to your local machine.

Add Your API Key
In the weather_app.py file, replace "YOUR_API_KEY" with your actual OpenWeatherMap API key.

Run the Application

```python
python weather_app.py
```
Use the App
Enter a city name in the input box and click Get Weather to view the current weather details.

## Code Explanation

Tkinter GUI: The app uses tkinter for the graphical interface, including labels, buttons, and entry widgets.
API Request: The app sends a GET request to the OpenWeatherMap API, including the city name, API key, and units (set to metric).
Display Results: Weather details (temperature, feels-like temperature, and description) are displayed in the interface upon a successful response.

# File Structure

```python
weather-app/
│
├── weather_app.py          # Main Python file with the weather app code
└── README.md               # Readme file with project details
```

## Example Usage

To try it out, simply enter a city name (e.g., "London") in the input field and click Get Weather. The app will display the current temperature, what it "feels like," and a short description of the weather (e.g., "clear sky").

## Screenshots

![Weather App Screenshot1](https://github.com/prkshdas/Weather-App-with-Tkinter/blob/main/web_app1.png)
![Weather App Screenshot2](https://github.com/prkshdas/Weather-App-with-Tkinter/blob/main/wed_app2.png)
![Weather App Screenshot3](https://github.com/prkshdas/Weather-App-with-Tkinter/blob/main/web_app3.png)

# Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!
