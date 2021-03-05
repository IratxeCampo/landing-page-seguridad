from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('memes/', views.memes, name='memes'),
    path('manopicaste/', views.manopicaste, name='manopicaste'),
    path('left-sidebar/', views.leftSide, name='left-sidebar'),
    path('right-sidebar/', views.rightSide, name='right-sidebar'),
    path('no-sidebar/', views.noSide, name='no-sidebar'),
]