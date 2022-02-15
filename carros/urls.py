from django.urls import path
from . import views 

urlpatterns = [
    path('', views.carros, name='carros'),
    path('<str:carro_url>', views.pagina_carro, name='pagina_carro'),
    path('pesquisa/', views.pesquisa, name='pesquisa'),
]
