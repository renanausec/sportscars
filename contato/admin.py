from django.contrib import admin
from .models import Contato

# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'carro_nome', 'cidade', 'create_date')
    list_display_links = ('id', 'nome', 'sobrenome')
    search_fields = ('nome', 'sobrenome', 'email', 'carro_nome')
    list_per_page = 25

admin.site.register(Contato, ContatoAdmin)