from django.urls import path
from . import views

urlpatterns = [
    path('<str:id_grupete>', views.main, name='index'),
    path('', views.main2, name='index2'),
    path('memes/', views.memes, name='memes'),
    path('manopicaste/', views.manopicaste, name='manopicaste'),
    path('phishing/', views.phishing, name='phishing'),
    path('otros-correos/', views.otrosCorreos, name='otros-correos'),
    path('experimento/', views.experimento, name='experimento'),
]