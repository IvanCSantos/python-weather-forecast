import requests
import json

location = input("Informe o nome da cidade que deseja a localização: ")
# Geocoding API
# https://openweathermap.org/api/geocoding-api
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
API_GEO = "http://api.openweathermap.org/geo/1.0/direct"
API_KEY="5253fb912cce5041e499f7a27f4cad17"
parameters = {
  "q" : location,
  "limit" : 1,
  "appid" : API_KEY
}
response = requests.get(API_GEO, params=parameters)
if(response.status_code == 200):
  latitude = response.json()[0]['lat']
  longitude = response.json()[0]['lon']

# Dados para Itajai / SC:
# https://www.google.com.br/maps/@-26.9162788,-48.6665522,16.47z
print("Latitude: " + str(latitude))
print("Longitude: " + str(longitude))

# Call curent weather data
# https://openweathermap.org/current
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
API_OWM = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
  "lat" : latitude,
  "lon" : longitude,
  "appid" : API_KEY,
  "lang" : "pt_br",
  "units" : "metric"
}
#response = requests.get(API_OWM, params=parameters)
#print(response.status_code)
#print(json.dumps(response.json(), indent=4))

# Call 5 day / 3 hour forecast data
# https://openweathermap.org/forecast5
# https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
API_FCST = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
  "lat" : latitude,
  "lon" : longitude,
  "appid" : API_KEY,
  "lang" : "pt_br",
  "units" : "metric"
}
response = requests.get(API_FCST, params=parameters)
print(response.status_code)
print(json.dumps(response.json(), indent=4))