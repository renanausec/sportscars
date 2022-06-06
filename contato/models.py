from datetime import datetime
from django.db import models
from datetime import datetime

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    car_id = models.IntegerField()
    carro_url = models.CharField(max_length=100)
    customer_need = models.CharField(max_length=100)
    carro_nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=100)
    mensagem = models.TextField(blank=True)
    user_id = models.IntegerField()
    create_date = models.DateTimeField(blank=True, default=datetime.now)

def __str__(self):
    return self.email