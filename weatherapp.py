
import requests
import json

key = '0b456bc491291527b0568143cd84085b'


class CityWeather:
    def __init__(self, city, longitude, latitude):
        self.city = city
        self.longitude = longitude
        self.latitude = latitude
        self.__CurrentWeather()


    def __CurrentWeather(self):
        url = 'https://api.darksky.net/forecast/%s/%s,%s?exclude=hourly,daily,hourly&lang=uk&units=si' \
              % (key, self.longitude, self.latitude)
        response = requests.get(url).json()['currently']
        with open('%s_weather.json' % self.city, 'w') as write_file:
            json.dump(response, write_file)
        self.current_temperature = round(response['temperature'])
        self.current_wind_speed = round(response['windSpeed'], 1)
        self.current_humidity = round((response['humidity'] * 100))

    def __PrintMessage__(self):
        message = "Current weather in %s:\n\n" \
                  "Current temperature: \t%s\xb0\tC\n" \
                  "Current wind speed: \t%s\tm/s\n" \
                  "Current humidity: \t\t%s\t%%" % (self.city, self.current_temperature, self.current_wind_speed,
                                                    self.current_humidity)
        print(message)


Kiev = CityWeather('Kiev', 50.431782, 30.516382)
Odessa = CityWeather('Odessa', 46.47747, 30.73262)

Kiev.__PrintMessage__()
print('=================================================')
Odessa.__PrintMessage__()
