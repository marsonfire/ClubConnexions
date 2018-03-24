from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Event

#this means the admin is logged in 
#it's really just for testing right now
enable = True

def index(request):
	return render(request, 'ama/index.html')

def home(request):
	return render(request, 'home/home.html')

def calendar(request):
	if(request.method == 'POST'):
		eventName = request.POST.get('eventName', None)
		eventDate = request.POST.get('eventDate', None)
		eventTime = request.POST.get('eventTime', None)
		eventLocation = request.POST.get('eventLocation', None)
		eventDescription = request.POST.get('eventDescription', None)
		e = Event.objects.create(eventName=eventName, eventDate=eventDate, eventTime=eventTime, eventLocation=eventLocation, eventDescription=eventDescription)
		allEvents = Event.objects.all()
		context = {'enable':enable, 'e':e, 'allEvents':allEvents}
		return render(request, 'calendar/calendar.html', context)

	#send to HTML if admin is logged in
	allEvents = Event.objects.all()
	context = {'enable':enable, 'allEvents':allEvents}
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

