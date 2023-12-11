from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Company, GovernAgency

# Create your views here.

def home(request):
    return render(request, "home.html")

def search(request):
    if request.method == "POST":
        search = request.POST['search_text']
        if search == "":
            return HttpResponseRedirect("/")
        company = Company.objects.filter(nome__icontains=search)
        govern = GovernAgency.objects.filter(nome__icontains=search)
        return render(request, "search.html", {"text": search, "company": company, "govern": govern})
    else:
        return HttpResponseRedirect("/")