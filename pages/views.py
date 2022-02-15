from django.shortcuts import render
from .models import Equipe
from carros.models import Carro

# Create your views here.

def home(request):
    equipes = Equipe.objects.all()
    featured_cars = Carro.objects.order_by('-data_add').filter(is_featured=True)
    all_cars = Carro.objects.order_by('-data_add')
    
    marca_pesquisa = Carro.objects.values_list('marca', flat=True).distinct()
    modelo_pesquisa = Carro.objects.values_list('modelo', flat=True).distinct()
    estado_pesquisa = Carro.objects.values_list('estado', flat=True).distinct()
    ano_pesquisa = Carro.objects.values_list('ano', flat=True).distinct()
    carroceria_pesquisa = Carro.objects.values_list('carroceria', flat=True).distinct()

    data = {
        'equipes': equipes,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'marca_pesquisa': marca_pesquisa,
        'modelo_pesquisa': modelo_pesquisa,
        'estado_pesquisa': estado_pesquisa,
        'ano_pesquisa': ano_pesquisa,
        'carroceria_pesquisa': carroceria_pesquisa,

    }
    return render(request, 'pages/home.html', data)
    
def sobre(request):
    return render(request, 'pages/sobre.html')

def parceiros(request):
    return render(request, 'pages/parceiros.html')

def contato(request):
    return render(request, 'pages/contato.html')