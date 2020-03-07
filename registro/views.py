from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')
