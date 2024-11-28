from django.contrib import admin
from stopwater.models import Registro

class Registros(admin.ModelAdmin):
    list_display = ['id', 'data_registro', 'nivel']
    list_display_links = ['id']

admin.site.register(Registro, Registros)
