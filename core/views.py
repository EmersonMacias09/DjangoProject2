from django.shortcuts import render
from .models import Proyecto, Persona

def home(request):
    persona = Persona.objects.first()
    return render(request, 'core/index.html', {'persona': persona})

def about(request):
    persona = Persona.objects.first()
    return render(request, 'core/about.html', {'persona': persona})

def contact(request):
    persona = Persona.objects.first()
    return render(request, 'core/contact.html', {'persona': persona})

def portfolio(request):
    persona = Persona.objects.first()
    proyectos = Proyecto.objects.all()
    return render(request, 'core/portfolio.html', {'persona': persona, 'proyectos': proyectos})