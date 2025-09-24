# weather.py
import requests
from config import API_KEY, BASE_URL

# Telangana districts coordinates (for Open-Meteo fallback)
CITY_COORDS = {
    "Adilabad": (19.6666, 78.5333),
    "Bhadradri Kothagudem": (17.5558, 80.6230),
    "Hyderabad": (17.3850, 78.4867),
    "Jagtial": (18.8000, 78.9333),
    "Jangaon": (17.7200, 79.1500),
    "Jayashankar Bhupalpally": (18.5500, 79.5833),
    "Jogulamba Gadwal": (16.1300, 77.8000),
    "Kamareddy": (18.3300, 78.3400),
    "Karimnagar": (18.4400, 79.1400),
    "Khammam": (17.2500, 80.1500),
    "Mahabubabad": (17.5500, 80.5500),
    "Mahabubnagar": (16.7300, 77.9800),
    "Mancherial": (19.2700, 79.4300),
    "Medak": (17.8200, 78.2700),
    "Medchal Malkajgiri": (17.5300, 78.6000),
    "Nagarkurnool": (16.5300, 78.3000),
    "Nalgonda": (17.0500, 79.2700),
    "Narayanpet": (16.9200, 77.5000),
    "Nirmal": (19.1000, 78.3500),
    "Nizamabad": (18.6700, 78.1000),
    "Peddapalli": (18.6200, 79.4000),
    "Rajanna Sircilla": (18.8200, 78.8300),
    "Rangareddy": (17.3500, 78.5000),
    "Sangareddy": (17.6000, 78.2700),
    "Siddipet": (18.1000, 78.8500),
    "Suryapet": (17.1500, 79.6200),
    "Vikarabad": (17.3500, 77.9000),
    "Wanaparthy": (16.3000, 78.0300),
    "Warangal Rural": (17.9700, 79.5700),
    "Warangal Urban": (17.9750, 79.5970),
    "Yadadri Bhuvanagiri": (17.5500, 78.9000)
}

def fetch_weather(city):
    """Try OpenWeatherMap first, fallback to Open-Meteo"""
    # --- Try OpenWeatherMap ---
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params, timeout=5)
        data = response.json()

        if response.status_code == 200:
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "condition": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }
        else:
            raise Exception(data.get("message", "OpenWeatherMap failed"))
    except:
        # --- Fallback to Open-Meteo ---
        if city not in CITY_COORDS:
            raise Exception(f"City '{city}' not mapped for Open-Meteo fallback!")

        lat, lon = CITY_COORDS[city]
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        resp = requests.get(url, timeout=5).json()
        current = resp.get("current_weather")
        if not current:
            raise Exception("Failed to fetch weather from Open-Meteo fallback")

        return {
            "city": city,
            "temperature": current["temperature"],
            "condition": f"Weather code {current['weathercode']}",
            "wind_speed": current["windspeed"] / 3.6  # km/h → m/s
        }

