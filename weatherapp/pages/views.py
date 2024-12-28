from django.shortcuts import render
from .forms import LocationForm
from configuration import Configuration

# Create your views here.
def home(request):
    form = LocationForm()
    return render(request, "pages/home.html", {"form":form})

def CurrentWeather(request):
    config = Configuration()
    api_key = config.get_api_key('api_key')
    host_url = config.host

    return render(request,"pages/results.html",{})