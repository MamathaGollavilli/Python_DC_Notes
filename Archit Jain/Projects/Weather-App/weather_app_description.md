# Weather App

## Project Overview

This Weather App is a simple Python script that fetches the current temperature for a given city using the WeatherAPI.

The project uses the `requests` library to make HTTP requests and the `dotenv` library to manage environment variables securely.

## Prerequisites

- Python 3
- `requests` library
- `python-dotenv` library
- A WeatherAPI API key

## Installation

1. **Clone the Repository**

2. **Navigate to the Project Directory**

3. **Install Required Python Packages**

   ```
   pip install requests python-dotenv
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the project directory and add your WeatherAPI API key:
   ```
   API_KEY=your_weatherapi_key
   ```

## How to Run

1. **Open a Terminal**

   Open a terminal and navigate to the project directory.

2. **Run the Script**

   Execute the script using Python:
   ```
   python weather_app.py
   ```

3. **Enter City Name**

   When prompted, enter the name of the city for which you want to get the current temperature.

4. **View Temperature**

   The script will display the current temperature for the specified city.

## Code Explanation

```python
import requests
import os
from dotenv import load_dotenv
import json
```
- **`requests`**: This module allows you to send HTTP requests. It's used to interact with the WeatherAPI.
- **`os`**: This module provides a way of using operating system-dependent functionality like reading environment variables.
- **`dotenv`**: This module allows you to read key-value pairs from a `.env` file and set them as environment variables.
- **`json`**: This module provides functions for parsing JSON data, which is the format in which the WeatherAPI returns data.

```python
city = input("Enter city name: ")
```
- This line prompts the user to enter the name of the city for which they want to get the weather information and stores it in the variable `city`.

```python
load_dotenv()
api_key = os.getenv("API_KEY")
```
- **`load_dotenv()`**: This function loads environment variables from a `.env` file into the environment.
- **`os.getenv("API_KEY")`**: This function retrieves the value of the environment variable `API_KEY` which should contain your WeatherAPI API key.

```python
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
```
- This line constructs the URL for the WeatherAPI request. It uses an f-string to insert the API key and city name into the URL.

```python
r = requests.get(url)
temp = json.loads(r.text)
```
- **`requests.get(url)`**: This function sends a GET request to the specified URL and returns the response.
- **`json.loads(r.text)`**: This function parses the JSON response from the WeatherAPI and converts it into a Python dictionary.

```python
print(f"Temperature: {temp['current']['temp_c']} C")
```
- This line extracts the current temperature in Celsius from the parsed JSON data and prints it to the console.

## Conclusion

This Weather App project demonstrates how to use Python to interact with an external API to fetch and display data. It covers basic input/output operations, making HTTP requests, handling JSON data, and managing environment variables securely.

---