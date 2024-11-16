#Write a program that fetches and prints out a random Chuck Norris joke for the user.
# Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.
import requests
response = requests.get("https://api.chucknorris.io/jokes/random").json()
print(response['value'])

#Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to
# write a program that asks the user for the name of a municipality and then prints out the corresponding
# weather condition description text and temperature in Celsius degrees. Take a good look at the API
# documentation. You must register for the service to receive the API key required for making API requests.
# Furthermore, find out how you can convert Kelvin degrees into Celsius.
import requests
import json
