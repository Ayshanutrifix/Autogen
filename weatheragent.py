import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    if not API_KEY:
        raise ValueError("❌ No API key found. Please add OPENWEATHER_API_KEY in .env")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"   # Celsius
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"].title()
        }
        return weather
    else:
        return {"error": f"Failed to fetch data: {response.status_code}, {response.text}"}

if __name__ == "__main__":
    city = input("Enter city name: ")
    result = get_weather(city)
    print(result)
