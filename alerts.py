def generate_alerts(temp, weather, wind_speed):
    alerts = []

    if temp > 40:
        alerts.append("🔥 Heatwave Alert!")
    if "rain" in weather.lower():
        alerts.append("☔ Heavy Rain Alert!")
    if wind_speed > 15:  # m/s ~ 54 km/h
        alerts.append("🌪️ Storm Alert!")

    if not alerts:
        alerts.append("✅ Weather looks normal.")

    return alerts
