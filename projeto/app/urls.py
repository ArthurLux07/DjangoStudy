from django.urls import path
from app.views import home
from app import views

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', views.cadastro, name='lista_cadastro'),
    
]
