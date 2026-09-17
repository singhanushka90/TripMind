import os
import requests

from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()


@tool
def get_flights(departure_airport: str, arrival_airport: str):
    """Get current flights between two airports using Aviationstack."""

    response = requests.get(
        "https://api.aviationstack.com/v1/flights",
        params={
            "access_key": os.getenv("AVIATION_API_KEY"),
            "dep_iata": departure_airport,
            "arr_iata": arrival_airport,
            "limit": 10
        },
        timeout=30
    )
    print("STATUS :",response.status_code)
    print("Response :",response.json())

    response.raise_for_status()

    data = response.json()

    if "error" in data:
        return {
            "error": data["error"]
        }

    flights = []

    for flight in data.get("data", []):
        flights.append({
            "airline": flight["airline"]["name"],
            "flight_number": flight["flight"]["iata"],
            "status": flight["flight_status"],
            "departure": flight["departure"]["airport"],
            "arrival": flight["arrival"]["airport"],
            "departure_time": flight["departure"]["scheduled"],
            "arrival_time": flight["arrival"]["scheduled"]
        })

    return {
        "flights": flights
    }

