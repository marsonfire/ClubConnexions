from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
	return render(request, 'ama/index.html')

def home(request):
	return render(request, 'home/home.html')

def calendar(request):
	return render(request, 'calendar/calendar.html')

def documents(request):
	return render(request, 'documents/documents.html')

def officers(request):
	return render(request, 'officers/officers.html')

def members(request):
	return render(request, 'members/members.html')

def login(request):
	return render(request, 'login/login.html')

