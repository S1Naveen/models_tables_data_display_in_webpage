from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topic(request):
    topics=Topic_view.objects.all()
    d={'topics':topics}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    web=Webpage_view.objects.all()
    d={'web':web}
    return render(request,'display_webpage.html',d)


def display_access(request):
    access=Access_view.objects.all()
    d={'access':access}
    return render(request,'display_access.html',d)