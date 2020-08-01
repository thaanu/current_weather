import requests
import datetime
import time

def get_weather( string: url ):
    weather_request = requests.get(url)
    weather_json = weather_request.json()

#    print(weather_json)

    description = weather_json['weather'][0]['description']
    humidity = weather_json['main']['humidity']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
    wind_speed = weather_json['wind']['speed']
    wind_degree = weather_json['wind']['deg']
    sunrise = weather_json['sys']['sunrise']
    sunset = weather_json['sys']['sunset']

    #coverting timestamp to time
    sundriseTime = datetime.datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
    sunsetTime = datetime.datetime.fromtimestamp(sunset).strftime('%H:%M:%S')

    print('Weather: ' +  str(description))
    print('Humidity: ' + str(humidity))
    print('Minimum Temperature: ' + str(temp_min))
    print('Maximum Temperature: ' + str(temp_max))
    print('Wind Speed: ' + str (wind_speed))
#    print('Wind Degree: ' + str(wind_degree))
    print('Sunrise: ' + str(sundriseTime))

# Run the function
get_weather( 'https://something.com' )
