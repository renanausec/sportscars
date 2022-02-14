from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')
    
def sobre(request):
    return render(request, 'pages/sobre.html')

def parceiros(request):
    return render(request, 'pages/parceiros.html')

def contato(request):
    return render(request, 'pages/contato.html')