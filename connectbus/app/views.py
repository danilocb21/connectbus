from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Company, GovernmentAgency

# Create your views here.

def home(request):
    return render(request, "home.html")

def search(request):
    if request.method == "GET":
        search: str = request.GET["search_query"]
        if not search:
            return HttpResponseRedirect("/")
        company = Company.objects.filter(user__first_name__icontains=search)
        government = GovernmentAgency.objects.filter(user__first_name__icontains=search)
        results: int = company.count() + government.count()
        return render(request, "search.html", {"text": search, "company": company, "government": government, "results": results})
    else:
        return HttpResponseRedirect("/")
    

def profile(request, username):
    return render(request, 'profile.html')