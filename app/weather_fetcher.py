from dotenv import load_dotenv
load_dotenv()
import requests
import os

def fetch_weather(location="San Francisco"):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    print("Using API key:", api_key)  # Add this for debugging
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": f"Failed to fetch weather: {response.status_code}"}
    
    data = response.json()
    weather = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    
    return {
        "location": location,
        "forecast": weather,
        "temperature": f"{temp}°F"
    }
