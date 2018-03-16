from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from ama.EventClass import *

#this means the admin is logged in 
#it's really just for testing right now
enable = True

e = Event("Test Name", "Test Date", "Test Time", "Test Location", "Test Description")
name = e.getName()

def index(request):
	return render(request, 'ama/index.html')

def home(request):
	return render(request, 'home/home.html')

def calendar(request):
	#send to HTML if admin is logged in
	context = {'enable':enable}
	return render(request, 'calendar/calendar.html', context)

def event(request):
	return render(request, 'calendar/event.html')

def documents(request):
	return render(request, 'documents/documents.html')

def officers(request):
	return render(request, 'officers/officers.html')

def members(request):
	return render(request, 'members/members.html')

def login(request):
	return render(request, 'login/login.html')

