import os
import requests
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()


def get_city_coordinates(city):
    response = requests.get(
        "https://api.geoapify.com/v1/geocode/search",
        params={
            "text": city,
            "format": "json",
            "apiKey": os.getenv("GEOAPIFY_API_KEY")
        }
    )

    data = response.json()
    location = data["results"][0]

    return location["lat"], location["lon"]


@tool
def get_places(city: str):
    """Get tourist places in a city."""

    lat, lon = get_city_coordinates(city)

    response = requests.get(
        "https://api.geoapify.com/v2/places",
        params={
            "categories": "tourism.sights",
            "filter": f"circle:{lon},{lat},20000",
            "limit": 10,
            "apiKey": os.getenv("GEOAPIFY_API_KEY")
        }
    )

    data = response.json()

    return {
        "city": city,
        "places": [
            feature["properties"].get("name")
            for feature in data.get("features", [])
        ]
    }

