from django.shortcuts import render

# Create your views here.

paths = []

count = 0

def main(request):

    global paths, count

    return render(request, 'appSeguWeb/index.html', {'title': 'Index'})

def memes(request):
    return render(request, 'appSeguWeb/memes.html', {'title': 'Memes'})

def manopicaste(request):
    return render(request, 'appSeguWeb/manopicaste.html', {'title': 'Mano Picaste'})

def noSide(request):
    return render(request, 'appSeguWeb/no-sidebar.html', {'title': 'No sidebar'})

def leftSide(request):
    return render(request, 'appSeguWeb/left-sidebar.html', {'title': 'Left sidebar'})

def rightSide(request):
    return render(request, 'appSeguWeb/right-sidebar.html', {'title': 'Right sidebar'})


