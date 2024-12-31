from django.shortcuts import render
from .forms import LocationForm
from configuration import Configuration
from .apps import CurrentWeather
from django.http import HttpResponseRedirect
from django.urls import reverse
import json

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})

def GetCurrentWeather(request):
    # Render input form
    form = LocationForm()
    currentweather = CurrentWeather()
    
    #Publish request
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            # Get location input from user
            location = request.POST.get('location')
            checkboxoption = request.POST.get('inlineRadioOptions')
            #Get WeatherAPI Response
            response = currentweather.GetCurrentWeatherAPIResponse(location)
        
            #render context
            context = {
                "form":LocationForm(),
                "response":response,
                "CurrentWeather":currentweather,
                "localtime": response['location']['localtime'].split(' ')[1],
                "checkboxoption": checkboxoption,
            }
            return render(request,"pages/currentweather.html",context)
    
    return render(request,"pages/currentweather.html",{"form":form})