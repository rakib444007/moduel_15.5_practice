
from django.http import HttpResponse
from django.shortcuts import render,redirect
from musician.models import Musician

def home(request):
    music =  Musician.objects.all()
    return render(request,'home.html',{'music' : music})