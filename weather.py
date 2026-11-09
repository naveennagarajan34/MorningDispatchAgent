import requests


def get_weather(latitude=11.034783, longitude=76.888031):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "timezone": "auto",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data.get("current", {})
        daily = data.get("daily", {})
        # Return only the essential numbers
        return {
            "current_temp_c": current.get("temperature_2m"),
            "humidity_pct": current.get("relative_humidity_2m"),
            "wind_speed_kmh": current.get("wind_speed_10m"),
            "max_temp_c": daily.get("temperature_2m_max", [None])[0],
            "min_temp_c": daily.get("temperature_2m_min", [None])[0],
            "rain_prob_pct": daily.get("precipitation_probability_max", [None])[0],
        }
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    print(get_weather())
