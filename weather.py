import requests

def fetch_weather(city):
    # Simple mapping for quick test (Hyderabad example)
    city_coords = {
        "Hyderabad": (17.385, 78.4867),
        "Delhi": (28.7041, 77.1025),
        "Mumbai": (19.076, 72.8777)
    }

    if city not in city_coords:
        raise Exception("City not mapped yet, add coordinates!")

    lat, lon = city_coords[city]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()

    if "current_weather" not in data:
        raise Exception("Failed to fetch weather")

    current = data["current_weather"]

    return {
        "city": city,
        "temperature": current["temperature"],
        "condition": f"Code {current['weathercode']}",  # numeric weather code
        "wind_speed": current["windspeed"] / 3.6  # km/h → m/s
    }
