import requests
import json


keyword = input("Enter the Municipality: ")
request = "api.openweathermap.org/data/2.5/weather?q="+keyword+",uk&APPID=f3030340c8d510be07322b293eecbb5f"

response = requests.get(request).json()
print(response)
