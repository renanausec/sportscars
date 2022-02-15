from django.contrib import admin
from .models import Equipe
from django.utils.html import format_html
# Register your models here.

class EquipeAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius: 50px" width="40" />'.format(object.photo.url))

        thumbnail.short_description = 'Foto'
    list_display = ('id', 'thumbnail', 'primeiro_nome', 'cargo', 'data_cadastro')
    list_display_links = ('id', 'thumbnail', 'primeiro_nome')
    search_fields = ('primeiro_nome', 'sobrenome', 'cargo')
    list_filter = ('cargo',)

admin.site.register(Equipe, EquipeAdmin)