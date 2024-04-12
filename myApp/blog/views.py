from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1> Blog Home Page')

def login(request):
    return HttpResponse('<h1> Blog Login Page </h1>')

def payment(request):

    return HttpResponse('<h1> Blog Payment Page </h1>')
