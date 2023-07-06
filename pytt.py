import requests
api_key = '47cd390e693044868c6154707232102'
# set up the API endpoint URL
# link = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q=kolkata'

# make a GET request to the API
response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={api_key}&q=kolkata')

# check if the response was successful
if response.status_code == 200:
    # extract the weather data
    print (response.json())
    