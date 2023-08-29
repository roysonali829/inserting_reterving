from django.shortcuts import render

from django.db.models.functions import Length
from app.models import *

# Create your views here.

def display_topic(request):
    QSTO = Topic.objects.all()
    d = {'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO = Webpage.objects.all()
    QSWO=Webpage.objects.filter(topic_name='Cricket')
    QSWO=Webpage.objects.exclude(topic_name='Cricket')
    QSWO=Webpage.objects.all().order_by('name')
    QSWO=Webpage.objects.filter(pk=3)
    QSWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    QSWO=Webpage.objects.all().order_by('-name')
    QSWO=Webpage.objects.all().order_by(Length('name'))

    QSWO=Webpage.objects.all().order_by(Length('name').desc())


    d = {'QSWO':QSWO}
    return render(request,'display_webpage.html',d)


def display_access(request):
    QSAO = AccessRecord.objects.all()
    d = {'QSAO':QSAO}
    return render(request,'display_access.html',d)


def Insert_Topic(request):
    tn = input('Enter the Topic : ')
    to = Topic.objects.get_or_create(topic_name = tn)[0]
    to.save()
    QSTO = Topic.objects.all()
    d = {'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def Insert_Webpage(request):
    tn = input('Enter the Topic : ')
    to = Topic.objects.get(topic_name = tn)
    to.save()
    n = input('Enter Name : ')
    u = input('Enter Url : ')
    wo = Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    QSWO = Webpage.objects.all()
    d = {'QSWO':QSWO}
    return render(request,'display_webpage.html',d)


def Insert_Access(request):
    tn = input('Enter the Topic : ')
    to = Topic.objects.get(topic_name = tn)
    pk=input('enter pk:')
    wo = Webpage.objects.get(topic_name=to,pk=pk)
    d = input('Enter Date : ')
    a = input('Enter Author : ')
    e = input('Enter Email : ')
    ao = AccessRecord.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    ao.save()
    QSAO = AccessRecord.objects.all()
    d = {'QSAO':QSAO}
    return render(request,'display_access.html',d)
