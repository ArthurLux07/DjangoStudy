from django.shortcuts import render 
from django.http import HttpResponse


def index(request):
    contexto = {
        'mensagem': "Bem-vindo ao sistema de cadastro de tarefas!"
    }
    return render(request, 'home.html', contexto)

