
# some imports
import json
import subprocess
import sys

# test to use microservice

# make subprocess call to service // example Portland
apiCall = subprocess.run([sys.executable, "APIcall.py", "45.523064", "-122.676483"], check=True,
                         stdout=subprocess.PIPE, text=True)
# grab output of data
jsonData = apiCall.stdout.strip()
weather_data = json.loads(jsonData)

# option to save data as json file
output_path = 'weatherData.json'
with open(output_path, 'w') as json_file:
    json.dump(weather_data, json_file, indent=2)

# use data
todayWeather = weather_data["weather"][0]["main"]
todayTemp = weather_data["main"]["temp_max"]
print(f"today's weather: {todayWeather}, and temp: {todayTemp} degrees fahrenheit.")
