from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from ama.EventClass import *

#this means the admin is logged in 
#it's really just for testing right now
enable = True

def index(request):
	return render(request, 'ama/index.html')

def home(request):
	return render(request, 'home/home.html')

def calendar(request):
	#send to HTML if admin is logged in
	context = {'enable':enable}
	return render(request, 'calendar/calendar.html', context)

def event(request):
	context = RequestContext(request)
	if (request.method == 'POST'):
		#getting it from the webpage
		form = Event(data = request.POST)
		name = request.POST.get('name')
		date = request.POST.get('date')
		time = request.POST.get('time')
		location = request.POST.get('location')
		description = request.POST.get('description')
		#creating an event object
		e = Event(name, date, time, location, description)
		#return render_to_response('calendar/event.html', {'name':name}, context)
		return render_to_response('calendar/event.html', {'name':name}, context)
	else:
		return render(request, 'calendar/event.html')

def documents(request):
	return render(request, 'documents/documents.html')

def officers(request):
	return render(request, 'officers/officers.html')

def members(request):
	return render(request, 'members/members.html')

def login(request):
	return render(request, 'login/login.html')

