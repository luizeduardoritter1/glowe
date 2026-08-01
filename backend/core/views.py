from django.shortcuts import render, get_object_or_404
from .models import Cliente, Agendamento

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})

def detalhe_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'core/detalhe_cliente.html', {'cliente': cliente})

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'core/lista_agendamentos.html', {'agendamentos': agendamentos})

