from django.urls import path

from . import views

app_name = 'ama'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name = 'home'),
    path('calendar/', views.calendar, name = 'calendar'),
    path('documents/', views.documents, name = 'documents'),
    path('officers/', views.officers, name = 'officers'),
    path('members/', views.members, name = 'members'),
    path('login/', views.login, name = 'login'),
]
