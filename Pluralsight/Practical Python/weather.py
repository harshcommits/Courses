import requests
import json

api_key = "3fea6b7575ccaf31b4183cbe0c3bb4db"
city = "Jaipur"

url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric"

request = requests.get(url)
json_data = request.json()

with open("weather.json", "w") as weather_file:
     json.dump(json_data, weather_file)

#print(json_data)

description = json_data.get("weather")[0].get("description")
print(f"The weather forecast for {city} today is {description}")