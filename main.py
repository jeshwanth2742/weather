# main.py
import streamlit as st
from weather import fetch_weather, CITY_COORDS
from alerts import generate_alerts

st.title("🌤️  Weather Alert ")

# Dropdown selection for Telangana districts
city = st.selectbox("Select a district", sorted(CITY_COORDS.keys()))

if st.button("Get Weather"):
    try:
        data = fetch_weather(city)
        st.subheader(f"🌍 Weather in {data['city']}")
        st.write(f"🌡️ Temperature: {data['temperature']} °C")
        st.write(f"☁️ Condition: {data['condition']}")
        st.write(f"💨 Wind Speed: {data['wind_speed']:.2f} m/s")

        st.subheader("🚨 Alerts:")
        for alert in generate_alerts(data['temperature'], data['condition'], data['wind_speed']):
            st.write(f"- {alert}")

    except Exception as e:
        st.error(f"Error fetching weather: {e}")

