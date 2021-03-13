from django.shortcuts import render
from django.http import HttpResponse
from .models import get_data

# Create your views here.
def index(request):
    if(request.method=="POST"):
        city_=request.POST["city"]
    else:
        city_= None
    weather=get_data()
    data=weather.weather(city_)
    return render(request,'index.html',{'data':data})
