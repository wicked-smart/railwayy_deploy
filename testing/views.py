from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("welcome to the show!!!")

def hello(request, name):
    return HttpResponse(f"Welcome {name}!!!")
