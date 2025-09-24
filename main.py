import sys
from weather import fetch_weather
from alerts import generate_alerts

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <city>")
        return

    city = " ".join(sys.argv[1:])

    try:
        weather_data = fetch_weather(city)
        alerts = generate_alerts(
            weather_data["temperature"],
            weather_data["condition"],
            weather_data["wind_speed"]
        )

        print(f"\n🌍 Weather in {weather_data['city']}:")
        print(f"🌡️ Temperature: {weather_data['temperature']} °C")
        print(f"☁️ Condition: {weather_data['condition']}")
        print(f"💨 Wind Speed: {weather_data['wind_speed']} m/s")

        print("\n🚨 Alerts:")
        for alert in alerts:
            print(f"- {alert}")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
