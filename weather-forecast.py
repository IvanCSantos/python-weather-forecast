import requests
import json
from datetime import datetime
import tkinter as tk

APP_NAME = "Python Weather Forecast"

def clearUserInput():
  pass

def confirmUserInput():
  pass

# Creating a Tkinter screen
root = tk.Tk()
root.title(APP_NAME)
root.geometry("600x300")
# Screen color=#2a82b4

# Defining and inserting user input field and buttons
userInput = tk.Entry(border=2, width=20, font=("Arial", 20)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)
btnOK = tk.Button(text="Confirmar", background="green", command=confirmUserInput).grid(row=0, column=2)
btnCancel = tk.Button(text="Limpar", background="green", command=clearUserInput).grid(row=0, column=3)

# Defining and inserting forecast data labels
today = tk.Label(text="Temperatura atual:").grid(row=1, column=0)
today = tk.Label(text="Hoje:").grid(row=2, column=0)
today = tk.Label(text="Previsão:").grid(row=3, column=0)
today = tk.Label(text="Descrição:").grid(row=4, column=0)
today = tk.Label(text="Máxima:").grid(row=5, column=0)
today = tk.Label(text="Mínima:").grid(row=6, column=0)


today = tk.Label(text="Amanhã").grid(row=2, column=1)

today = tk.Label(text="Depois").grid(row=2, column=2)

today = tk.Label(text="Depois2").grid(row=2, column=3)

today = tk.Label(text="Depois3").grid(row=2, column=4)


# Program loop
root.mainloop()


# ------ 

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

forecasts = []
for weather in response.json()['list']:
  day = datetime.fromtimestamp(weather['dt']).day
  min = weather['main']['temp_min']
  max = weather['main']['temp_max']
  main = str(weather['weather'][0]['main'])
  description = str(weather['weather'][0]['description'])
  if(len(forecasts) >= 1):
    if(forecasts[-1]['day'] == day):
      if(forecasts[-1]['min'] > min):
        forecasts[-1]['min'] = min
      if(forecasts[-1]['max'] < max):
        forecasts[-1]['max'] = max
      if(main == 'Rain'):
        forecasts[-1]['main'] = main
        forecasts[-1]['description'] = description
      if(main == 'Clouds' and forecasts[-1]['main'] != 'Rain'):
        forecasts[-1]['main'] = main
        if(forecasts[-1]['main'] != 'Clouds'):
          forecasts[-1]['description'] = description
        else:
          if(forecasts[-1]['description'] != 'nublado' and description == 'nublado'):
            forecasts[-1]['description'] = description
      continue
  forecasts.append({
    'day' : day,
    'min' : min,
    'max' : max,
    'main' : main,
    'description' : description
  })

print("\n\n")
for forecast in forecasts:
  print("Dia: " + str(forecast['day']) + ":")
  #print("Temperatura: " + str(forecast['temp']))
  print("Mínima: " + str(forecast['min']) + "°")
  print("Máxima: " + str(forecast['max']) + "°")
  print("Previsão: " + str(forecast['main']))
  print("Descrição: " + str(forecast['description']))
  print("\n")

#DEBUG
#for weather in response.json()['list']:
#  print(str(datetime.fromtimestamp(weather['dt'])) + "--> " + weather['dt_txt'])
#for weather in response.json()['list']:
#  print(str(datetime.fromtimestamp(weather['dt'])) + ", " + str(weather['main']['temp']) + ", " + str(weather['main']['temp_min']) + ", " + str(weather['main']['temp_max']) + ", " + str(weather['weather'][0]['main']) + ", " + str(weather['weather'][0]['description']))
#print(json.dumps(response.json(), indent=4))