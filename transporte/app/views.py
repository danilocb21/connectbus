from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello World</h1>")