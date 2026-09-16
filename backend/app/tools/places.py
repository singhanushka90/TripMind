from langchain_core.tools import tool

@tool
def get_places(city:str):
    """Get popular tourist places in a give city."""
    return {
        "city":city,
        "places":["Baga Beach","Fort Aguada","Dudhsagar Falls","Basilica of Bom Jesus"]
    }