from django.contrib import admin
from .models import Persona, Proyecto

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'correo', 'titulo_academico']

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'enlace']