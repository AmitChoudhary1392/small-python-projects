from django.apps import AppConfig
from configuration import Configuration
import requests


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'

class CurrentWeather(Configuration):
    def __init__(self):
        Configuration.__init__(self)
        self.location = ''
        self.region =''
        self.country = ''
        self.temp_c = ''
        self.temp_f = ''
        self.feelslike_c = ''
        self.feelslike_f = ''
        self.weather_icon = ''
        self.weather_code = ''
        self.wind_speed = ''
        self.wind_direction = ''
    
    def GetCurrentWeatherAPIResponse(self,location=None):
        base_url = self.host
        api_key = self.get_api_key('api_key')
        
        if not location:
            return "Please input location to search current weather conditions"

        if location:
            curr_weather_url = base_url + f'/current.json?key={api_key}&q={location}'
            response = requests.get(curr_weather_url).json()
            self.location = response['location']['name']
            self.region = response['location']['region']
            self.country = response['location']['country']
            self.temp_c = response['current']['temp_c']
            self.temp_f = response['current']['temp_f']
            self.feelslike_c = response['current']['feelslike_c']
            self.feelslike_f = response['current']['feelslike_f']
            self.weather_icon = response['current']['condition']['icon']
            self.weather_code = response['current']['condition']['code']
            self.wind_speed = response['current']['wind_kph']
            self.wind_direction = response['current']['wind_dir']
            
            return response
        
    def __repr__(self):
        return f'{self.location} | Temp:{self.temp_c}'
