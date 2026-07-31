from django.shortcuts import render
from .models import Cliente, Agendamento

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'core/lista_agendamentos.html', {'agendamentos': agendamentos})

