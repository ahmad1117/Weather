import requests
API_KEY = "1a6fcadcfaeac9f4ee288de5a4a640d6"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" # OpenWeatherMap API endpoint 
city = input("Enter city name: ") # User input for city name
request_url  = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric" # Constructing the request URL with city name and API key
response = requests.get(request_url)
if response.status_code == 200:
    data  = response.json()
    weather = data['weather'][0]['description']  # Extracting weather description
    temp = data['main']['temp']
    humidity = data['main']['humidity']  # Extracting humidity
    wind_speed = data['wind']['speed']  # Extracting wind speed
    print(f"\nWeather in {city.title()}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("City not found. Please check the city name and try again.")