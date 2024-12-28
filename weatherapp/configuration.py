import apikey
import sys

class Configuration():
    def __init__(self):
        # default url
        self.host = "https://api.weatherapi.com/v1"
        self.api_key = {}

    def get_api_key(self, identifier):

        try:
            key = apikey.keyObject[identifier]
            return key

        except ValueError:
            raise ValueError('Api Key Identifier is not valid')

    def auth_settings(self):
        
        return {
            'ApiKey':{
                'type':'api_key',
                'key':'key',
                'value':self.get_api_key('api_key')
            }
        }