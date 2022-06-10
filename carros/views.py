from django.shortcuts import get_object_or_404, render
from .models import Carro
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def carros(request):
    carros = Carro.objects.order_by('-data_add')
    paginator = Paginator(carros, 4)
    page = request.GET.get('page')
    carros_paginados = paginator.get_page(page)

    marca_pesquisa = Carro.objects.values_list('marca', flat=True).distinct()
    modelo_pesquisa = Carro.objects.values_list('modelo', flat=True).distinct()
    estado_pesquisa = Carro.objects.values_list('estado', flat=True).distinct()
    ano_pesquisa = Carro.objects.values_list('ano', flat=True).distinct()
    carroceria_pesquisa = Carro.objects.values_list('carroceria', flat=True).distinct()

    data = {
        'carros': carros_paginados,
        'marca_pesquisa': marca_pesquisa,
        'modelo_pesquisa': modelo_pesquisa,
        'estado_pesquisa': estado_pesquisa,
        'ano_pesquisa': ano_pesquisa,
        'carroceria_pesquisa': carroceria_pesquisa,
    }
    return render(request, 'carros/carros.html', data)

def pagina_carro(request, carro_url):
    single_car = get_object_or_404(Carro, carro_url=carro_url)

    data = {
        'single_car': single_car,
    }
    return render(request, 'carros/pagina_carro.html', data)

def pesquisa(request):
    carros = Carro.objects.order_by('-data_add')
    marca_pesquisa = Carro.objects.values_list('marca', flat=True).distinct()
    modelo_pesquisa = Carro.objects.values_list('modelo', flat=True).distinct()
    estado_pesquisa = Carro.objects.values_list('estado', flat=True).distinct()
    ano_pesquisa = Carro.objects.values_list('ano', flat=True).distinct()
    carroceria_pesquisa = Carro.objects.values_list('carroceria', flat=True).distinct()
    transmissao_pesquisa = Carro.objects.values_list('transmissao', flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            carros = carros.filter(carro_nome__icontains=keyword)

    if 'marca' in request.GET: #aqui é pego o valor que está no option da pagina home
        marca= request.GET['marca']
        if marca:
            carros = carros.filter(marca__iexact=marca)

    if 'modelo' in request.GET: #aqui é pego o valor que está no option da pagina home
        modelo = request.GET['modelo']
        if modelo:
            carros = carros.filter(modelo__iexact=modelo)
            
    if 'estado' in request.GET: #aqui é pego o valor que está no option da pagina home
        estado = request.GET['estado']
        if estado:
            carros = carros.filter(estado__iexact=estado)
            
    if 'ano' in request.GET: #aqui é pego o valor que está no option da pagina home
        ano = request.GET['ano']
        if ano:
            carros = carros.filter(ano__iexact=ano)
            
    if 'carroceria' in request.GET: #aqui é pego o valor que está no option da pagina home
        carroceria = request.GET['carroceria']
        if carroceria:
            carros = carros.filter(carroceria__iexact=carroceria)

    if 'transmissao' in request.GET: #aqui é pego o valor que está no option da pagina home
        transmissao = request.GET['transmissao']
        if transmissao:
            carros = carros.filter(transmissao__iexact=transmissao)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            carros = carros.filter(preco__gte=min_price, preco__lte=max_price) # __gte greater than / __lte lower than
            
    data = {
        'carros': carros,    
        'marca_pesquisa': marca_pesquisa,
        'modelo_pesquisa': modelo_pesquisa,
        'estado_pesquisa': estado_pesquisa,
        'ano_pesquisa': ano_pesquisa,
        'carroceria_pesquisa': carroceria_pesquisa,
        'transmissao_pesquisa': transmissao_pesquisa,
    }
    return render(request, 'carros/pesquisa.html', data)
