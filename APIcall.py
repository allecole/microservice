# microservice
# developed nov 18, 2023 by cole allen
# calls on API service with longitude and latitude.

# imports
import json
import sys
import requests


def APIservice(lat, lon):
    """microservice that calls on weather API providing data based on coordinates"""
    # api key
    apiKey = "451316d4db2c0980eeb4f0c0ace4a4dc"
    # api request
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}&units=imperial'

    # write the api request into a json file
    response = requests.get(url)

    # send error message if request request fails
    if response.status_code != 200:
        print(f"Error: '{response.status_code}'. PLease enter valid location")
    else:  # if request succeeds
        # send json file with weather data
        weatherData = response.json()
        print(json.dumps(weatherData, indent=2))


if __name__ == "__main__":
    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])
    APIservice(latitude, longitude)

