from django.contrib import admin
from .models import Inquiry, Contato

# Register your models here.

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'carro_nome', 'cidade', 'create_date')
    list_display_links = ('id', 'nome', 'sobrenome')
    search_fields = ('nome', 'sobrenome', 'email', 'carro_nome')
    list_per_page = 25

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'create_date')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'email', 'assunto')
    list_per_page = 25

admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Contato, ContatoAdmin)