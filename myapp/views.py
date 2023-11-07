from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1> hey , welcome to my site </h1>')
