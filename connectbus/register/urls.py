from django.urls import path
from .views import *

urlpatterns = [
    path('', register, name="register_choice_page"),
    path('client', register_client, name="register_client_page"),
    path('company', register_company, name="register_company_page")
]
