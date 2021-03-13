from django.db import models
import requests

# Create your models here.
class get_data:
    def __init__(self):
        self.url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8a60f97907057f9ec1f2cb3697be4c37'
    def weather(self,name):
        if(not name):
            return {'country_code' : 0}
        try:
            r = requests.get(self.url.format(name)).json()
            temp=(int(r['main']['temp'])-32)*(5/9)
            temp=float("{:.2f}".format(temp))
            weather = {'city' : name,'temperature' : str(temp),
            'description' : r['weather'][0]['description'].capitalize(),'country_code' : r['cod']}
            return weather
        except:
            return {'country_code' : 0}
