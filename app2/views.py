from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<marquee><h1> This is a first project </h1></maequee>')

def second(request):
    return HttpResponse('<h1> Have a nice day </h1>')
