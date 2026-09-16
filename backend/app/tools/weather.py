from langchain_core.tools import tool
import requests


@tool
def get_weather(city:str):
    """Get the current weather for a given city using Open-Meteo."""
    geo_response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search",
                                params={
                                    "name":city,
                                    "count":1,
                                    "language":"en",
                                    "format":"json",
                                    "countryCode":"IN"
                                },
                                timeout=10
                    )
    geo_response.raise_for_status()
    geo_data=geo_response.json()

    if not geo_data.get("results"):
        return {
            "error":f"City '{city}' not found."
        }
    location=geo_data["results"][0]
    latitude=location["latitude"]
    longitude=location["longitude"]

    weather_response=requests.get("https://api.open-meteo.com/v1/forecast",params={
        "latitude":latitude,
        "longitude":longitude,
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m","timezone":"auto"
    },
    timeout=10
    )
    weather_response.raise_for_status()
    weather_data=weather_response.json()
    current=weather_data["current"]


    return {
        "city":location["name"],
        "country":location.get("country"),
        "temperature":current["temperature_2m"],
        "humidity":current["relative_humidity_2m"],
        "condition":current["weather_code"],
        "wind_speed":current["wind_speed_10m"]
    }

if __name__=="__main__":
    result=get_weather.invoke({"city":"Goa"})
    print(result)