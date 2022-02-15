from random import choice, choices
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.forms import BooleanField, DateField, DateTimeField, IntegerField

# Create your models here.
class Carro(models.Model):

    state_choice = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    )

    year_choice = []
    for r in range(1900, (datetime.now().year+2)):
        year_choice.append((r,r))

    transmissao_choices = (
        ('Automática', 'Automática'),
        ('Manual', 'Manual'),
    )
    recursos_choices = (
        ('Controle de Tração', 'Controle de Tração'),
        ('Sensor de Estacionamento', 'Sensor de Estacionamento'),
        ('Airbags', 'Airbags'),
        ('Ar Condicionado', 'Ar Condicionado'),
        ('Bancos com Aquecimento', 'Bancos com Aquecimento'),
        ('Difusor de Escapamento', 'Difusor de Escapamento'),
        ('ParkAssist', 'ParkAssist'),
        ('Camera de Ré', 'Camera de Ré'),
        ('Sensor de Estacionamento Traseiro', 'Sensor de Estacionamento Traseiro'),
        ('Sensor de Estacionamento Dianteiro', 'Sensor de Estacionamento Dianteiro'),
        ('Start/Stop', 'Start/Stop'),
        ('Sensor de Colisão', 'Sensor de Colisão'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    carro_nome = models.CharField(max_length=255)
    carro_url = models.CharField(max_length=255, blank=True)
    estado = models.CharField(choices=state_choice, max_length=100)
    cidade = models.CharField(max_length=150)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField(('ano'), choices=year_choice)
    carroceria = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    transmissao = models.CharField(choices=transmissao_choices, max_length=100)
    recursos = MultiSelectField(choices=recursos_choices, blank=True)
    outros_recursos = models.CharField(max_length=100, blank=True)
    interior = models.CharField(max_length=100)
    km = models.IntegerField()
    combustivel = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    preco = models.IntegerField()
    preco_promo = models.IntegerField(blank=True)
    seo_alt = models.CharField(max_length=100)
    seo_meta = models.CharField(max_length=255)
    descricao = RichTextField()
    car_photo = models.ImageField(upload_to='fotos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    car_photo_5 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    car_photo_6 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    car_photo_7 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    car_photo_8 = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    data_add = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.carro_nome