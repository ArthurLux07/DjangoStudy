# views.py
from django.shortcuts import render, redirect
from .models import InfoCad
from .forms import InfoCadForm

def home(request):
    return render(request, 'home/home.html', {'form': InfoCadForm()})

def cadastro(request):
    if request.method == 'POST':
        form = InfoCadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cadastro')  
    else:
        form = InfoCadForm()

    cadastros = InfoCad.objects.all()
    
    return render(request, 'home/cadastro.html', {
        'cadastros': cadastros,   
        'form': form
    })