import os
import requests

from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()


@tool
def get_hotels(
    city: str,
    check_in: str,
    check_out: str,
    adults: int = 2
):
    """Search hotels in a city using Google Hotels through SerpApi."""

    api_key = os.getenv("SERP_API_KEY")

    response = requests.get(
        "https://serpapi.com/search",
        params={
            "engine": "google_hotels",
            "q": f"{city} hotels",
            "check_in_date": check_in,
            "check_out_date": check_out,
            "adults": adults,
            "children": 0,
            "currency": "INR",
            "gl": "in",
            "hl": "en",
            "api_key": api_key
        },
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    if "error" in data:
        return {
            "error": data["error"]
        }

    hotels = []

    for hotel in data.get("properties", [])[:10]:
        hotels.append({
            "name": hotel.get("name"),
            "rating": hotel.get("overall_rating"),
            "reviews": hotel.get("reviews"),
            "price_per_night": hotel.get("rate_per_night", {}).get("lowest"),
            "total_price": hotel.get("total_rate", {}).get("lowest"),
            "amenities": hotel.get("amenities", []),
            "link": hotel.get("link")
        })

    return {
        "city": city,
        "check_in": check_in,
        "check_out": check_out,
        "hotels": hotels
    }
