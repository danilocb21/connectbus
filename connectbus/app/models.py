from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cpf_id = models.CharField(max_length=11, unique=True)
    primary_phone = models.CharField(max_length=11)
    optional_phone = models.CharField(max_length=11, blank=True)
    birth_date = models.DateField()
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=100)
    # name = models.CharField(max_length=200)
    # email = models.EmailField(max_length=100, unique=True)
    # password = models.CharField(max_length=128)

    def __str__(self):
        return self.user.first_name

class GovernmentAgency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=11)
    # name = models.CharField(max_length=200)
    # email = models.EmailField(max_length=100, unique=True)
    # password = models.CharField(max_length=128)

    def __str__(self):
        return self.user.first_name

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cnpj_id = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=11)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    # name = models.CharField(max_length=200)
    # email = models.EmailField(max_length=100, unique=True)
    # password = models.CharField(max_length=128)

    def __str__(self):
        return self.user.first_name

class TypeFeedback(models.Model):
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id)

class Feedback(models.Model):
    feedback_type = models.ForeignKey(TypeFeedback, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    government_agency = models.ForeignKey(GovernmentAgency, on_delete=models.CASCADE)
    observation = models.TextField()
    complaint_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Status(models.IntegerChoices):
        NEW = 0
        PENDING = 1
        COMPLETE = 2
        CANCELLED = 99
    
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

class CompanyFeedback(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
