import requests
import json


location = input("Informe o nome da cidade que deseja a localização: ")
# Geocoding API
# https://openweathermap.org/api/geocoding-api
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
API_GEO = "http://api.openweathermap.org/geo/1.0/direct"
parameters = {
  "q" : location,
  "limit" : 5,
  "appid" : "5253fb912cce5041e499f7a27f4cad17"
}
response = requests.get(API_GEO, params=parameters)
print(response.status_code)
#print(response.json())
#print(json.dumps(response.json(), indent=4))
#print(json.dumps(response.json()[0]["lat"], indent=4))
#response = json.dumps(response.json(), indent=4)
#print(response.json())
latitude = response.json()[0]['lat']
longitude = response.json()[0]['lon']
# Itajai:
# https://www.google.com.br/maps/@-26.9162788,-48.6665522,16.47z
print("Latitude: " + str(latitude))
print("Longitude: " + str(longitude))


# Call curent weather data
# https://openweathermap.org/current
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#lat="latitude"
#lon="longitude"
#API_KEY="key"
#API = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=" + API_KEY
API_OWM = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
  "lat" : "latitude",
  "lon" : "longitude",
  "appid" : "5253fb912cce5041e499f7a27f4cad17"
}
#print(API)

#response = requests.get(API_OWM, params=parameters)
#print(response.status_code)
#print(response.json())
#print(json.dumps(response.json(), indent=4))