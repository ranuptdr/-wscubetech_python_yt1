from django.http import HttpResponse
from django.shortcuts import render

def homePage(requst):
    data={
        'title' : 'Home Page New',
        'bdata' : 'Welcome to Wscubetech',
        'clist' : ['PHP', 'Java', 'Django'],
        'student_details' : [
            {'name' : 'ranu', 'phone':1234567899},
            {'name' : 'ygsh', 'phone':9987456321}
        ]
    }
    return render(requst,"index.html",data)

def aboutUs(requst):
    return HttpResponse("Welcome To Home")

def myApp(requst):
    return HttpResponse("<b>Welcome To MyApp</b>") # <b>....bold krna....</b>

def appDetails(requst,appid):
    return HttpResponse(appid)
