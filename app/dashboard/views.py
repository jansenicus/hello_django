from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the dashboard!</h1><p>This is the home page of the dashboard app.</p>")
