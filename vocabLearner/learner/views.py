from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(req):
    return HttpResponse("yo this is the landing page")
