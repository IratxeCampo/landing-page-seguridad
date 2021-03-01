from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('elements/', views.elements, name='elements'),
    path('left-sidebar/', views.leftSide, name='left-sidebar'),
    path('right-sidebar/', views.rightSide, name='right-sidebar'),
    path('no-sidebar/', views.noSide, name='no-sidebar'),
]