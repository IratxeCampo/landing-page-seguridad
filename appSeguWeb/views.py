from django.shortcuts import render

# Create your views here.

paths = []

count = 0

def main(request):

    global paths, count

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
