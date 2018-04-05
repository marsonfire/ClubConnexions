from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Event
from .models import Officers
from .models import Members

#this means the admin is logged in 
#it's really just for testing right now
enable = True

def index(request):
	return render(request, 'ama/index.html')

def home(request):
	return render(request, 'home/home.html')

def calendar(request):
	allEvents = Event.objects.all()
	if(request.POST.get('addEvent')):
		eventName = request.POST.get('eventName', None).strip()
		eventDate = request.POST.get('eventDate', None).strip()
		eventTime = request.POST.get('eventTime', None).strip()
		eventLocation = request.POST.get('eventLocation', None).strip()
		eventDescription = request.POST.get('eventDescription', None).strip()
		e = Event.objects.create(eventName=eventName, eventDate=eventDate, eventTime=eventTime, eventLocation=eventLocation, eventDescription=eventDescription)
		context = {'enable':enable, 'e':e, 'allEvents':allEvents}
		return render(request, 'calendar/calendar.html', context)
	elif(request.GET.get('deleteAllEvents')):
		for e in allEvents:
			e.delete()
	elif(request.POST.get('deleteEvent')):
		eventName = request.POST.get('eventName', None).strip()
		for e in allEvents:
			if(e.eventName == eventName):
				e.delete()
	context = {'enable':enable, 'allEvents':allEvents}
	return render(request, 'calendar/calendar.html', context)

def event(request):
	return render(request, 'calendar/event.html')

def documents(request):
	return render(request, 'documents/documents.html')

def officers(request):
	if(request.method == 'POST'):
		officerFirstName = request.POST.get('officerFirstName', None).strip()
		officerLastName = request.POST.get('officerLastName', None).strip()
		officerPosition = request.POST.get('officerPosition', None).strip()
		o = Officers.objects.create(officerFirstName=officerFirstName, officerLastName=officerLastName, officerPosition=officerPosition)
		allOfficers = Officers.objects.all()
		context = {'enable':enable, 'o':o, 'allOfficers':allOfficers}
		return render(request, 'officers/officers.html', context)
		
	allOfficers = Officers.objects.all()
	context = {'enable':enable, 'allOfficers':allOfficers}
	return render(request, 'officers/officers.html', context)

def addOfficer(request):
	return render(request, 'officers/addOfficer.html')

def members(request):
	if(request.method == 'POST'):
		memberFirstName = request.POST.get('memberFirstName', None)
		memberLastName = request.POST.get('memberLastName', None)
		m = Members.objects.create(memberFirstName=memberFirstName, memberLastName=memberLastName)
		allMembers = Members.objects.all()
		context = {'enable':enable, 'm':m, 'allMembers':allMembers}
		return render(request, 'members/members.html', context)
		
	allMembers = Members.objects.all()
	context = {'enable':enable, 'allMembers':allMembers}
	return render(request, 'members/members.html', context)

def addMember(request):
	return render(request, 'members/addMember.html')

def login(request):
	return render(request, 'login/login.html')

def password(request):
        if(request.method==('login')):
                loginAttempt= request.POST.get('password',None)
                if(loginAttempt == 'currentPassword'):
                   render(request,'login/password.html')     
        
        return render(request, 'login/password.html' )

def changePassword(request):
        return render(request, 'login/changePassword.html')
                
