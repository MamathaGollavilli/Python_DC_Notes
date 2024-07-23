import requests
import os
from dotenv import load_dotenv, dotenv_values
import json

city = input("Enter city name: ")
load_dotenv()
api_key = os.getenv("API_KEY")
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

r = requests.get(url)
temp = json.loads(r.text)
print(f"Temperature: {temp['current']['temp_c']} C")
