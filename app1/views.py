from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first(request):
    return HttpResponse('<marquee><h1> hey!! This is Vruta </h1></marquee>')
def second(request):
    return HttpResponse('<i><h1> Good Morning </h1></i>')
