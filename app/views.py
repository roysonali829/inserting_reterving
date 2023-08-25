from django.shortcuts import render

from app.models import *

from django.http import HttpResponse
# Create your views here.

def Insert_Topic(request):
    tn = input('Enter the Topic : ')
    to = Topic.objects.get_or_create(topic_name = tn)[0]
    to.save()
    return HttpResponse('Data Inserted')

def Insert_Webpage(request):
    tn = input('Enter the Topic : ')
    to = Topic.objects.get_or_create(topic_name = tn)[0]
    to.save()
    n = input('Enter Name : ')
    u = input('Enter Url : ')
    wo = Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('Data Inserted')

def Insert_AccessRecord(request):
    tn = input('Enter the Topic : ')
    to = Topic.objects.get_or_create(topic_name = tn)[0]
    to.save()
    n = input('Enter Name : ')
    u = input('Enter Url : ')
    wo = Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d = input('Enter Date : ')
    a = input('Enter Author : ')
    e = input('Enter Email : ')
    ao = AccessRecord.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    ao.save()
    return HttpResponse('Data Inserted')



def display_topics(request):
    QSTO = Topic.objects.all()
    d = {'QSTO':QSTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QSWO = Webpage.objects.all()
    d = {'QSWO':QSWO}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    QSAO = AccessRecord.objects.all()
    d = {'QSAO':QSAO}
    return render(request,'display_accessrecords.html',d)
