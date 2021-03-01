from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'appSeguWeb/index.html', {'title': 'Index'})

def elements(request):
    return render(request, 'appSeguWeb/elements.html', {'title': 'Elements'})

def noSide(request):
    return render(request, 'appSeguWeb/no-sidebar.html', {'title': 'No sidebar'})

def leftSide(request):
    return render(request, 'appSeguWeb/left-sidebar.html', {'title': 'Left sidebar'})

def rightSide(request):
    return render(request, 'appSeguWeb/right-sidebar.html', {'title': 'Right sidebar'})


