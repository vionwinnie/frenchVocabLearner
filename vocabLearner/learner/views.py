from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here

def index(req):
    return HttpResponse("yo this is the landing page")


def content(req):
    return HttpResponse("the content of the article here")



