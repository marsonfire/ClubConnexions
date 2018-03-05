from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the Home Page\nTo get to Calendar, go to http://localhost:8000/calendar/\nTo get to Documents, go to http://localhost:8000/documents/\nTo get to Officer Info, go to http://localhost:8000/officers/\nTo get to Club Members, go to http://localhost:8000/members/\nTo get to Admin Login, go to http://localhost:8000/login/")
