import requests
import json



# Request template: https://api.chucknorris.io/jokes/random?category={category}
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(response["value"])