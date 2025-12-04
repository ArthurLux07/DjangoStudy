from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import InfoCad
from .forms import InfoCadForm

def home(request):
    return render(request, 'home/home.html', {'form': InfoCadForm()})


def lista_cadastros(request):
    cadastros = InfoCad.objects.all().order_by('-id')
    return render(request, 'home/cadastro.html', {'cadastros': cadastros})


def adicionar(request):
    if request.method == 'POST':
        form = InfoCadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro adicionado com sucesso!')
            return redirect('lista_cadastro')
    else:
        form = InfoCadForm()
    return render(request, 'home/home.html', {'form': form})


def editar(request, pk):
    pessoa = get_object_or_404(InfoCad, pk=pk)
    if request.method == 'POST':
        form = InfoCadForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro atualizado com sucesso!')
            return redirect('lista_cadastro')
    else:
        form = InfoCadForm(instance=pessoa)
    
    return render(request, 'home/editar.html', {'form': form, 'pessoa': pessoa})


def deletar(request, pk):
    pessoa = get_object_or_404(InfoCad, pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        messages.success(request, 'Cadastro excluído com sucesso!')
        return redirect('lista_cadastro')
    
    return render(request, 'home/deletar.html', {'pessoa': pessoa})