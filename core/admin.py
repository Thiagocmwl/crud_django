from django.contrib import admin
from .models import Pessoa


class AdminPessoa(admin.ModelAdmin):
    list_display = ['nome', 'idade', 'peso', 'genero', 'criacao', 'alteracao', 'mostrar']
    list_editable = ('genero', 'mostrar')


admin.site.register(Pessoa, AdminPessoa)
