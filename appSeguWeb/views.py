from django.shortcuts import render, redirect
from .models import Grupete, LasHoras
from datetime import datetime

# Create your views here.

def main(request):

    if len(request.GET) == 0:
        pass
    elif len(request.GET) == 1:
        grupete = Grupete.objects.filter(id_grupete=request.GET["c"])
        if len(grupete) > 0: # ouyeah pillamos [0], megachapuza
            datetaim = datetime.now() # TO-DO
            grupete[0].visitas += 1
            grupete[0].save()
            lashorejas = LasHoras.objects.create(grupete=grupete[0], datetime_acceso=datetaim) # TO-DO
            lashorejas.save()
    else:
        pass

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