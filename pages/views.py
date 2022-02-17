from django.shortcuts import render, redirect
from .models import Equipe
from carros.models import Carro
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    featured_cars = Carro.objects.order_by('-data_add').filter(is_featured=True)
    all_cars = Carro.objects.order_by('-data_add')
    
    marca_pesquisa = Carro.objects.values_list('marca', flat=True).distinct()
    modelo_pesquisa = Carro.objects.values_list('modelo', flat=True).distinct()
    estado_pesquisa = Carro.objects.values_list('estado', flat=True).distinct()
    ano_pesquisa = Carro.objects.values_list('ano', flat=True).distinct()
    carroceria_pesquisa = Carro.objects.values_list('carroceria', flat=True).distinct()

    data = {
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
    equipes = Equipe.objects.all()
    data = {
        'equipes': equipes,
        }
    return render(request, 'pages/sobre.html', data)

def parceiros(request):
    return render(request, 'pages/parceiros.html')

def contato(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        assunto = request.POST['assunto']
        mensagem = request.POST['mensagem']

        assunto_email = 'Contato SportsCars - ' + assunto
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        message_body = 'Nome: '  + nome + '. E-mail: ' + email + '. Telefone: ' + telefone + '.  Mensagem: ' + mensagem
 
        send_mail(
            assunto_email,
            message_body,
            'renanr.ausec@gmail.com',
            [admin_email],
            fail_silently=False
        )        
        messages.success(request, 'Obrigado pelo seu contato! Responderemos o mais rápido possível!')
        return redirect( 'contato')
    return render(request, 'pages/contato.html')