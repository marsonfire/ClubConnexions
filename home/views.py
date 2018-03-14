from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Description

# Create your views here.
#Instructions text will show up on the webpage but will be hard to read since
#it's unformatted. Here's an easier way to see stuff:
#To get to Home, go to http://localhost:8000/home/
#To get to Calendar, go to http://localhost:8000/calendar/
#To get to Documents, go to http://localhost:8000/documents/
#To get to Officer Info, go to http://localhost:8000/officers/
#To get to Club Members, go to http://localhost:8000/members/
#To get to Admin Login, go to http://localhost:8000/login/"

#Testing Stuff cuz GIT HUB IS SO ANNOYING
def index(request):
    desc = Description.descriptionText
    template = loader.get_template('home/index.html')
    context = {
        'desc':desc,
    }
    return HttpResponse(template.render(context, request))
