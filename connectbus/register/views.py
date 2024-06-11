from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, RegisterClientForm, RegisterCompanyForm, CustomAuthenticationForm
from app.models import Client, Company

# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return render(request, "registration/logout.html")

def register(request):
    user = request.user
    if (user.is_authenticated):
        return redirect("/")
    
    if (request.method == "POST"):
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            form = form.cleaned_data
            request.session["form"] = form
            if request.POST["user_type"] == "client":
                return redirect("/register/client")
            return redirect("/register/company")
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form":form})

def register_client(request):
    user_form = request.session.get("form")
    if user_form:
        if request.method == "POST":
            form = RegisterClientForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                first_name = form["first_name"]
                last_name = form["last_name"]
                birth_date = form["birth_date"]
                cpf_id = form["cpf"]
                primary_phone = form["primary_phone"]
                optional_phone = form["optional_phone"]
                street = form["street"]
                number = form["number"]
                neighborhood = form["neighborhood"]
                user = User(
                    username=user_form["username"],
                    email=user_form["email"],
                    password=user_form["password1"],
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                client = Client(
                    user=user,
                    cpf_id=cpf_id,
                    birth_date=birth_date,
                    primary_phone=primary_phone,
                    optional_phone=optional_phone,
                    street=street,
                    number=number,
                    neighborhood=neighborhood
                )
                login(request, user)
                client.save()
                request.session.pop('form', None)
                return redirect("/")
            else:
                print(form.errors)
        else:
            form = RegisterClientForm()
        
        return render(request, "registerclient.html", {"form":form})
    
    elif request.user.is_authenticated:
        return redirect("/")
    
    return redirect("/register")

def register_company(request):
    user_form = request.session.get("form")
    if user_form:
        if request.method == "POST":
            form = RegisterCompanyForm(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                name = form["name"]
                cnpj_id = form["cnpj"]
                phone = form["phone"]
                street = form["street"]
                number = form["number"]
                user = User(
                    username=user_form["username"],
                    email=user_form["email"],
                    password=user_form["password1"],
                    first_name=name,
                )
                user.save()
                company = Company(
                    user=user,
                    cnpj_id=cnpj_id,
                    phone=phone,
                    street=street,
                    number=number,
                )
                login(request, user)
                company.save()
                request.session.pop('form', None)
                return redirect("/")
            else:
                print(form.errors)
        else:
            form = RegisterCompanyForm()
        
        return render(request, "registercompany.html", {"form":form})
    
    elif request.user.is_authenticated:
        return redirect("/")
    
    return redirect("/register")


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm