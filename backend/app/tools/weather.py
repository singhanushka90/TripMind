from langchain_core.tools import tool


@tool
def get_weather(city:str):
    """Get the current weather for a given city."""
    return {
        "city":city,
        "temperature":29,
        "condition":"Cloudy"
    }