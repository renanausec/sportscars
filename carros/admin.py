from django.contrib import admin
from .models import Carro
from django.utils.html import format_html

# Register your models here.
class CarroAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius: 10px" width="40" />'.format(object.car_photo.url))

        thumbnail.short_description = 'Foto do Carro'

    list_display = ('carro_nome', 'thumbnail', 'estado', 'cidade', 'ano', 'is_featured')
    list_display_links = ('carro_nome', 'thumbnail')
    search_fields = ('carro_nome', 'estado', 'cidade', 'ano')
    list_editable = ('is_featured',)
    list_filter = ('cidade',)
admin.site.register(Carro, CarroAdmin)