from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Company, GovernmentAgency

# Create your views here.

def home(request):
    return render(request, "home.html")

def search(request):
    if request.method == "POST":
        search = request.POST['search_text']
        if search == "":
            return HttpResponseRedirect("/")
        company = Company.objects.filter(nome__icontains=search)
        government = GovernmentAgency.objects.filter(nome__icontains=search)
        resultados = company.count() + government.count()
        return render(request, "search.html", {"text": search, "company": company, "government": government, "resultados": resultados})
    else:
        return HttpResponseRedirect("/")
    

def perfil(request, username):
    return render(request, 'perfil.html')