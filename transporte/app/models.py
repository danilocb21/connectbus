from django.db import models

# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    telefone_principal = models.CharField(max_length=11)
    telefone_opcional = models.CharField(max_length=11, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)
    datansc = models.DateField()
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class GovernAgency(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Service(models.Model):
    descricao = models.CharField(max_length=200)
class Company(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class TypeFeedback(models.Model):
    descricao = models.CharField(max_length=200)

class Feedback(models.Model):
    tipo = models.ForeignKey(TypeFeedback, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    org = models.ForeignKey(GovernAgency, on_delete=models.CASCADE)
    observacao = models.TextField()
    data_reclamacao = models.DateTimeField(auto_now_add=True)
    class Status(models.IntegerChoices):
        NEW = 0
        PENDING = 1
        COMPLETE = 2
        CANCELLED = 99
    status = models.IntegerField(choices=Status.choices, default=Status.NEW)

class FBCompany(models.Model):
    reclamacao = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Company, on_delete=models.CASCADE)
    