from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login

from .models import Event
from .models import Officers
from .models import Members
from .models import Home

def index(request):
	return render(request, 'ama/index.html')

def home(request):
	return render(request, 'home/home.html')

def editHome(request):
	if(request.user.is_authenticated):
		return render(request, 'home/editHome.html')
	else:
		return redirect('/ama/home')

def calendar(request):
	allEvents = Event.objects.all()
	if(request.POST.get('addEvent')):
		eventName = request.POST.get('eventName', None).strip()
		eventDate = request.POST.get('eventDate', None).strip()
		eventTime = request.POST.get('eventTime', None).strip()
		eventLocation = request.POST.get('eventLocation', None).strip()
		eventDescription = request.POST.get('eventDescription', None).strip()
		e = Event.objects.create(eventName=eventName, eventDate=eventDate, eventTime=eventTime, eventLocation=eventLocation, eventDescription=eventDescription)
		context = {'e':e, 'allEvents':allEvents}
		return render(request, 'calendar/calendar.html', context)
	elif(request.GET.get('deleteAllEvents')):
		for e in allEvents:
			e.delete()
			return redirect('/ama/calendar/')

	elif(request.POST.get('deleteEvent')):
		eventName = request.POST.get('eventName', None).strip()
		for e in allEvents:
			if(e.eventName == eventName):
				e.delete()
				return redirect('/ama/calendar/')
	context = {'allEvents':allEvents}
	return render(request, 'calendar/calendar.html', context)

def event(request):
	if(request.user.is_authenticated):
		return render(request, 'calendar/event.html')
	else:
		return redirect('/ama/home')

def documents(request):
	return render(request, 'documents/documents.html')

def officers(request):
	allOfficers = Officers.objects.all()
	if(request.POST.get('addOfficer')):
		officerFirstName = request.POST.get('officerFirstName', None).strip()
		officerLastName = request.POST.get('officerLastName', None).strip()
		officerPosition = request.POST.get('officerPosition', None).strip()
		o = Officers.objects.create(officerFirstName=officerFirstName, officerLastName=officerLastName, officerPosition=officerPosition)
		allOfficers = Officers.objects.all()
		context = {'o':o, 'allOfficers':allOfficers}
		return render(request, 'officers/officers.html', context)
	elif(request.POST.get('deleteOfficer')):
		officerName = request.POST.get('officerName', None).strip()
		for o in allOfficers:
			officerObjName = o.officerFirstName + " " + o.officerLastName
			if(officerObjName == officerName):
				o.delete()
				return redirect('/ama/officers/')
	elif(request.GET.get('deleteAllOfficers')):
		for o in allOfficers:
			o.delete()
		return redirect('/ama/officers')
	context = {'allOfficers':allOfficers}
	return render(request, 'officers/officers.html', context)

def addOfficer(request):
	if(request.user.is_authenticated):
		return render(request, 'officers/addOfficer.html')
	else:
		return redirect('/ama/home')

def members(request):
	if(request.user.is_authenticated):
		allMembers = Members.objects.all()
		if(request.POST.get('addMember')):
			memberFirstName = request.POST.get('memberFirstName', None)
			memberLastName = request.POST.get('memberLastName', None)
			memberEmail = request.POST.get('memberEmail', None)
			memberID = request.POST.get('memberID', None)
			email = request.POST.get('email', None)
			allCardNumber = request.POST.get('allCardNumber', None)
			m = Members.objects.create(memberFirstName=memberFirstName, memberLastName=memberLastName, memberEmail=memberEmail, memberID=memberID)
			allMembers = Members.objects.all()
			context = {'m':m, 'allMembers':allMembers}
			return render(request, 'members/members.html', context)
		elif(request.POST.get('deleteMember')):
			memberName = request.POST.get('memberName', None).strip()
			for m in allMembers:
				memberObjName = m.memberFirstName + " " + m.memberLastName
				if(memberName == memberObjName):
					m.delete()
					return redirect('/ama/members/')
		elif(request.GET.get('deleteAllMembers')):
			for m in allMembers:
				m.delete()
			return redirect('/ama/members')

		context = {'allMembers':allMembers}
		return render(request, 'members/members.html', context)
	else:
		return redirect('/ama/home')

def addMember(request):
	if(request.user.is_authenticated):
		return render(request, 'members/addMember.html')
	else:
		return redirect('/ama/home')


def login(request):
	if(request.POST.get('logout')):
		logout(request)
		return redirect('/ama/login/')
	return render(request, 'login/login.html')

def password(request):
	if(request.POST.get('login')):
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		user = authenticate(request, username=username, password=password)
		if(user is not None):
			auth_login(request, user)
			return redirect('/ama/home')
	return render(request, 'login/password.html')

def changePassword(request):
	if(request.user.is_authenticated):
		return render(request, 'login/changePassword.html')
	else:
		return redirect('/ama/home')        
