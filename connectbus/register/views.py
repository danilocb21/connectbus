from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, CustomAuthenticationForm

# Create your views here.
def register(request):
    user = request.user
    if (user.is_authenticated):
        return redirect("/")
    
    if (request.method == "POST"):
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            login(request, user)

            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form":form})

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm