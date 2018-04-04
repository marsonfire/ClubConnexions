from django.urls import path

from . import views

app_name = 'ama'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name = 'home'),
    path('calendar/', views.calendar, name = 'calendar'),
    path('calendar/add-event', views.event, name = 'add-event'),
    path('documents/', views.documents, name = 'documents'),
    path('officers/', views.officers, name = 'officers'),
    path('officers/add-officer', views.addOfficer, name = 'add-officer'),
    path('members/', views.members, name = 'members'),
    path('members/add-member', views.addMember, name = 'add-member'),
    path('login/', views.login, name = 'login'),
    path('password/', views.password, name= 'password'),
]
