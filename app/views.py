from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *

def display_topic(request):
    topics=Topic_view.objects.all()
    topics=Topic_view.objects.filter(topic_name='cricket')
    d={'topics':topics}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    web=Webpage_view.objects.all()
    web=Webpage_view.objects.filter(id='1')
    web=Webpage_view.objects.exclude(id='2')
    web=Webpage_view.objects.all()[::3]
    web=Webpage_view.objects.all()[::-1]
    web=Webpage_view.objects.all().order_by('name')
    web=Webpage_view.objects.all().order_by('-name')
    web=Webpage_view.objects.all().order_by(Length('name'))
    web=Webpage_view.objects.all().order_by(Length('name').desc())

    d={'web':web}
    return render(request,'display_webpage.html',d)


def display_access(request):
    access=Access_view.objects.all()
    d={'access':access}
    return render(request,'display_access.html',d)