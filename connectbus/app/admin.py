from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(GovernmentAgency)
admin.site.register(Company)
admin.site.register(TypeFeedback)
admin.site.register(Feedback)