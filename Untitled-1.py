import requests

# replace YOUR_API_KEY with your actual API key
api_key = '47cd390e693044868c6154707232102'

# set up the API endpoint URL
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q=Hyderabad'

# make a GET request to the API
response = requests.get(url)

# check if the response was successful
if response.status_code == 200:
    # extract the weather data from the JSON response
    weather_data = response.json()

    # extract the temperature in Celsius
    temperature = weather_data['current']['temp_c']

    # extract the weather condition description
    description = weather_data['current']['condition']['text']

    # print the weather information
    print(f'The temperature in Hyderabad is {temperature}°C and the weather condition is {description}.')
else:
    print('Error: Could not retrieve weather data.')
