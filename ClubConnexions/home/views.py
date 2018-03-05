from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Instructions text will show up on the webpage but will be hard to read since
#it's unformatted. Here's an easier way to see stuff:
#To get to Home, go to http://localhost:8000/home/
#To get to Calendar, go to http://localhost:8000/calendar/
#To get to Documents, go to http://localhost:8000/documents/
#To get to Officer Info, go to http://localhost:8000/officers/
#To get to Club Members, go to http://localhost:8000/members/
#To get to Admin Login, go to http://localhost:8000/login/"
def index(request):
    return HttpResponse("Welcome to the Home Page\nTo get to Calendar, go to http://localhost:8000/calendar/\nTo get to Documents, go to http://localhost:8000/documents/\nTo get to Officer Info, go to http://localhost:8000/officers/\nTo get to Club Members, go to http://localhost:8000/members/\nTo get to Admin Login, go to http://localhost:8000/login/")
