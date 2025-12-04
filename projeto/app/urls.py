from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.lista_cadastros, name='lista_cadastro'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:pk>/', views.editar, name='editar'),
    path('deletar/<int:pk>/', views.deletar, name='deletar'),
]