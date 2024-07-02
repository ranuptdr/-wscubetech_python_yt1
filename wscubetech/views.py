from django.http import HttpResponse
from django.shortcuts import render

def homePage(requst):
    return render(requst,"index.html")

def aboutUs(requst):
    return HttpResponse("Welcome To Home")

def myApp(requst):
    return HttpResponse("<b>Welcome To MyApp</b>") # <b>....bold krna....</b>

def appDetails(requst,appid):
    return HttpResponse(appid)
