from django.contrib import admin
from django.urls import path
from app.views import home
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro_usuario'),
]
