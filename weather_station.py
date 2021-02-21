import requests
import time

class WeatherStation:
    def __init__(self, location):
        self.location = location
        openWeatherParameters = {
            'q': self.location,
            'appid': 'e66d4b8b6712e0812ebc3a43a3b4b843',
            'units': 'metric'
        }
        self.response = requests.get('http://api.openweathermap.org/data/2.5/weather', openWeatherParameters)
        # print(self.response.json())
        self.response_code = self.response.json()['cod']

    def get_coordinated(self):
        """This returns latitude and longitude as a tuple"""
        return (self.response.json()['coord']['lat'], self.response.json()['coord']['lon'])

    def get_description(self):
        """This returns the description of the weather"""
        return self.response.json()['weather'][0]['description'].title()

    def get_temperature(self):
        """This returns minimum, current, and maximum temperature as a tuple"""
        return (self.response.json()['main']['temp_min'], self.response.json()['main']['temp'],
                self.response.json()['main']['temp_max'])

    def get_pressure(self):
        """This returns the pressure value"""
        return self.response.json()['main']['pressure']

    def get_humidity(self):
        """This returns the humidity value"""
        return self.response.json()['main']['humidity']

    def get_visibility(self):
        """This returns visibility value"""
        return self.response.json()['visibility']

    def get_wind_speed(self):
        """This returns wind speed"""
        return round(self.response.json()['wind']['speed']*3.6, 2)

    def get_location(self):
        """This returns City, Country as a tuple"""
        return (self.response.json()['name'], self.response.json()['sys']['country'])

    def get_daytime(self):
        """This returns Sunrise, and Sunset as a tuple in local time"""
        return (f"{time.localtime(self.response.json()['sys']['sunrise'])[3]}:"
                f"{time.localtime(self.response.json()['sys']['sunrise'])[4]}",
                f"{time.localtime(self.response.json()['sys']['sunset'])[3]}:"
                f"{time.localtime(self.response.json()['sys']['sunset'])[4]}")

    def get_timezone(self):
        """This returns timezone in unix UTC"""
        return self.response.json()['timezone']

