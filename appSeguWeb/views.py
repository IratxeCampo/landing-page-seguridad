from django.shortcuts import render, get_object_or_404
from .models import Grupete, LasHoras
from datetime import datetime

# Create your views here.

def main(request, id_grupete):

    datetaim = datetime.now()

    grupete = Grupete.objects.get(id_grupete=id_grupete)
    grupete.visitas += 1
    grupete.save()

    lashorejas = LasHoras.objects.create(grupete=grupete, datetime_acceso=datetaim)
    lashorejas.save()

    return render(request, 'appSeguWeb/index.html', {'title': 'Ataque de phishing'})

def main2(request):
    return render(request, 'appSeguWeb/index.html', {'title': 'Ataque de phishing'})

def memes(request):
    return render(request, 'appSeguWeb/memes.html', {'title': 'Memes'})

def manopicaste(request):
    return render(request, 'appSeguWeb/manopicaste.html', {'title': 'Picaste'})

def experimento(request):
    return render(request, 'appSeguWeb/experimento.html', {'title': '¿De qué va este experimento?'})

def phishing(request):
    return render(request, 'appSeguWeb/phishing.html', {'title': '¿Qué es un ataque de phising?'})

def otrosCorreos(request):
    return render(request, 'appSeguWeb/otros-correos.html', {'title': '¿Qué otros correos hemos utilizado?'})

def view_404(request, exception):
    return render(request, 'appSeguWeb/404.html', {'title': 'Error 404'})