from django.shortcuts import render
from .models import MeetingMinutes, Meeting, Resource, Event

# Create your views here.
def index (request):
    return render(request, 'Club/index.html')

def getevents(request):
    event_list = Event.objects.all()
    return render(request, 'Club/events.html', {'event_list': event_list})