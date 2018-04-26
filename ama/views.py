from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.core.mail import EmailMessage

from .models import Event
from .models import Officers
from .models import Members
from .models import Home

def index(request):
	return render(request, 'ama/index.html')

def home(request):
	return render(request, 'home/home.html')

def editHome(request):
	return render(request, 'home/editHome.html')

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
	return render(request, 'calendar/event.html')

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
	return render(request, 'officers/addOfficer.html')

def members(request):
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
	elif(request.POST.get('sendNotification')):
		# subject = request.POST.get('subject', None)
		# message = request.POST.get('message', None)
		# sender = 'schatzk@xavier.edu'
		# recipients = ['schatzk@xavier.edu']
		# # allMembers = Members.objects.all()
		# # for m in allMembers:
		# # 	reipients.append(m.memberEmail)
		# send_mass_mail((subject,message,sender,recipients), fail_silently=False)
		# email = EmailMessage('subject','message',to=['schatzk@xavier.edu'])
		# email.send()

		subject = 'test'
		message = 'please work'
		from_email = settings.EMAIL_HOST_USER
		to_list = ['kkmarie62@gmail.com']
		send_mail(subject, message, from_email, to_list, fail_silently=True)

		return render(request, 'members/members.html', context)
	context = {'allMembers':allMembers}
	return render(request, 'members/members.html', context)

def addMember(request):
	return render(request, 'members/addMember.html')

def sendNotification(request):
	return render(request, 'members/sendNotification.html')

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
			return redirect('/ama/login/password')
	return render(request, 'login/password.html')

def changePassword(request):
	return render(request, 'login/changePassword.html')
                
