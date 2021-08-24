from django.shortcuts import render, redirect
from .form import UsuarioForm
from registro.models import*

# Create your views here.

def inicio(request):
    if request.method == 'GET':
        form = UsuarioForm
        contexto = {
        'form' : form
        }
    else:
        form = UsuarioForm(request.POST)
        contexto = {
        'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('registro:lista')
    return render(request, 'registroform/registro.html', contexto)


def lista(request):
    return render(request, 'lista/listaequipos.html', {"equipos":UsuarioEquipos.objects.all})