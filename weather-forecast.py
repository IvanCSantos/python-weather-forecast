import requests
import json
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk

APP_NAME = "Python Weather Forecast"
API_GEO = "http://api.openweathermap.org/geo/1.0/direct"
API_FCST = "https://api.openweathermap.org/data/2.5/forecast"
API_OWM = "https://api.openweathermap.org/data/2.5/weather"
API_KEY="5253fb912cce5041e499f7a27f4cad17"

# Creating a Tkinter screen
root = Tk()
root.title(APP_NAME)
root.geometry("600x300")
# Screen color=#2a82b4


def getGeoLocation(locationName):
  #location = input("Informe o nome da cidade que deseja a localização: ")
  location = locationName
  # Geocoding API
  # https://openweathermap.org/api/geocoding-api
  # http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
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
  #print("Latitude: " + str(latitude))
  #print("Longitude: " + str(longitude))
  return latitude, longitude


def getCurrentWeather(latitude, longitude):
  # Call curent weather data
  # https://openweathermap.org/current
  # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
  parameters = {
    "lat" : latitude,
    "lon" : longitude,
    "appid" : API_KEY,
    "lang" : "pt_br",
    "units" : "metric"
  }
  response = requests.get(API_OWM, params=parameters)
  #print(response.status_code)
  #print(json.dumps(response.json(), indent=4))
  currentTemp = response.json()['main']['temp']
  currentWeather = response.json()['weather'][0]['main']
  return {'temp' : currentTemp, 'weather' : currentWeather}


def getFiveDaysForecast(latitude, longitude):
  # Call 5 day / 3 hour forecast data
  # https://openweathermap.org/forecast5
  # https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
  parameters = {
    "lat" : latitude,
    "lon" : longitude,
    "appid" : API_KEY,
    "lang" : "pt_br",
    "units" : "metric"
  }
  response = requests.get(API_FCST, params=parameters)
  #print(response.status_code)
  forecasts = []
  for weather in response.json()['list']:
    day = datetime.fromtimestamp(weather['dt']).day
    month = datetime.fromtimestamp(weather['dt']).month
    date = str(day) + "/" + str(month)
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
      'day' : date,
      'min' : min,
      'max' : max,
      'main' : main,
      'description' : description
    })
  return forecasts
  #print("\n\n")
  #for forecast in forecasts:
  #  print("Dia: " + str(forecast['day']) + ":")
  #  #print("Temperatura: " + str(forecast['temp']))
  #  print("Mínima: " + str(forecast['min']) + "°")
  #  print("Máxima: " + str(forecast['max']) + "°")
  #  print("Previsão: " + str(forecast['main']))
  #  print("Descrição: " + str(forecast['description']))
  #  print("\n")

#DEBUG
#for weather in response.json()['list']:
#  print(str(datetime.fromtimestamp(weather['dt'])) + "--> " + weather['dt_txt'])
#for weather in response.json()['list']:
#  print(str(datetime.fromtimestamp(weather['dt'])) + ", " + str(weather['main']['temp']) + ", " + str(weather['main']['temp_min']) + ", " + str(weather['main']['temp_max']) + ", " + str(weather['weather'][0]['main']) + ", " + str(weather['weather'][0]['description']))
#print(json.dumps(response.json(), indent=4))

def updateScreenForecast(currentWeather, fiveDaysForecast):
  print(fiveDaysForecast)
  # Day 1
  currentTemp.set(str(currentWeather['temp']) + "°")
  description1.set(str(fiveDaysForecast[0]['description']))
  day1.set(str(fiveDaysForecast[0]['day']))
  min1.set("Min: " + str(fiveDaysForecast[0]['min']) + "°")
  max1.set("Max: " + str(fiveDaysForecast[0]['max']) + "°")

  # Day 2
  description2.set(str(fiveDaysForecast[1]['description']))
  day2.set(str(fiveDaysForecast[1]['day']))
  min2.set("Min: " + str(fiveDaysForecast[1]['min']) + "°")
  max2.set("Max: " + str(fiveDaysForecast[1]['max']) + "°")

  # Day 3
  description3.set(str(fiveDaysForecast[2]['description']))
  day3.set(str(fiveDaysForecast[2]['day']))
  min3.set("Min: " + str(fiveDaysForecast[2]['min']) + "°")
  max3.set("Max: " + str(fiveDaysForecast[2]['max']) + "°")

  # Day 4
  description4.set(str(fiveDaysForecast[3]['description']))
  day4.set(str(fiveDaysForecast[3]['day']))
  min4.set("Min: " + str(fiveDaysForecast[3]['min']) + "°")
  max4.set("Max: " + str(fiveDaysForecast[3]['max']) + "°")

  # Day 5
  description5.set(str(fiveDaysForecast[4]['description']))
  day5.set(str(fiveDaysForecast[4]['day']))
  min5.set("Min: " + str(fiveDaysForecast[4]['min']) + "°")
  max5.set("Max: " + str(fiveDaysForecast[4]['max']) + "°")


def clearUserInput():
  userInput.delete(0, END)
  currentTemp.set("")
  description1.set("")
  day1.set("")
  min1.set("")
  max1.set("")
  description2.set("")
  day2.set("")
  min2.set("")
  max2.set("")
  description3.set("")
  day3.set("")
  min3.set("")
  max3.set("")
  description4.set("")
  day4.set("")
  min4.set("")
  max4.set("")
  description5.set("")
  day5.set("")
  min5.set("")
  max5.set("")


def confirmUserInput():
  location = userInput.get()
  latitude, longitude = getGeoLocation(location)
  fiveDaysForecast = getFiveDaysForecast(latitude, longitude)
  currentWeather = getCurrentWeather(latitude, longitude)
  updateScreenForecast(currentWeather, fiveDaysForecast)
  userInput.delete(0, END)

# Defining and inserting user input field and buttons
userInput = Entry(border=2, width=20, font=("Arial", 20))
userInput.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
btnOK = Button(text="Confirmar", background="green", command=confirmUserInput).grid(row=0, column=2)
btnCancel = Button(text="Limpar", background="green", command=clearUserInput).grid(row=0, column=3)

# Defining and inserting forecast data labels
#currentWeatherImg = Image.open("cloud.png")
#currentWeatherPicture = ImageTk.PhotoImage(currentWeatherImg)
#currentWeather = Label(image=currentWeatherPicture)
#currentWeather.grid(row=1, column=0)

## Day 1
# Current temperature
currentTemp = StringVar()
currentTemp.set("")
lblCurrentTemp = Label(textvariable=currentTemp, font=("Arial", 22)).grid(row=1, column=0)

# Temperature description
description1 = StringVar()
description1.set("")
lbldescription1 = Label(textvariable=description1).grid(row=3, column=0)

# Date
day1 = StringVar()
day1.set("")
lblDay1 = Label(textvariable=day1, font=("Arial", 16)).grid(row=4, column=0)

# Min
min1 = StringVar()
min1.set("")
lblMin1 = Label(textvariable=min1).grid(row=5, column=0)

# Max
max1 = StringVar()
max1.set("")
lblMax1 = Label(textvariable=max1).grid(row=6, column=0)

## Day 2
# Temperature description
description2 = StringVar()
description2.set("")
lbldescription2 = Label(textvariable=description2).grid(row=3, column=1)

# Date
day2 = StringVar()
day2.set("")
lblDay2 = Label(textvariable=day2, font=("Arial", 16)).grid(row=4, column=1)

# Min
min2 = StringVar()
min2.set("")
lblMin2 = Label(textvariable=min2).grid(row=5, column=1)

# Max
max2 = StringVar()
max2.set("")
lblMax2 = Label(textvariable=max2).grid(row=6, column=1)

## Day 3
# Temperature description
description3 = StringVar()
description3.set("")
lbldescription3 = Label(textvariable=description3).grid(row=3, column=2)

# Date
day3 = StringVar()
day3.set("")
lblDay3 = Label(textvariable=day3, font=("Arial", 16)).grid(row=4, column=2)

# Min
min3 = StringVar()
min3.set("")
lblMin3 = Label(textvariable=min3).grid(row=5, column=2)

# Max
max3 = StringVar()
max3.set("")
lblMax3 = Label(textvariable=max3).grid(row=6, column=2)

## Day 4
# Temperature description
description4 = StringVar()
description4.set("")
lbldescription4 = Label(textvariable=description4).grid(row=3, column=3)

# Date
day4 = StringVar()
day4.set("")
lblDay4 = Label(textvariable=day4, font=("Arial", 16)).grid(row=4, column=3)

# Min
min4 = StringVar()
min4.set("")
lblMin4 = Label(textvariable=min4).grid(row=5, column=3)

# Max
max4 = StringVar()
max4.set("")
lblMax4 = Label(textvariable=max4).grid(row=6, column=3)

## Day 5
# Temperature description
description5 = StringVar()
description5.set("")
lbldescription5 = Label(textvariable=description5).grid(row=3, column=4)

# Date
day5 = StringVar()
day5.set("")
lblDay5 = Label(textvariable=day5, font=("Arial", 16)).grid(row=4, column=4)

# Min
min5 = StringVar()
min5.set("")
lblMin5 = Label(textvariable=min5).grid(row=5, column=4)

# Max
max5 = StringVar()
max5.set("")
lblMax5 = Label(textvariable=max5).grid(row=6, column=4)

# Program loop
root.mainloop()