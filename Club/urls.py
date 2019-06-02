from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getevents/', views.getevents, name = 'events'),
    path('getresources/', views.getresources, name = 'resources'),
    path('getmeetings/', views.getmeetings, name = 'meetings'),
]