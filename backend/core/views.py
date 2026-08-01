# views.py — as "funções de resposta".
# Cada view recebe um pedido (request) do navegador, busca os dados que precisa
# e devolve uma página pronta.

from django.shortcuts import render, get_object_or_404, redirect  # atalhos úteis do Django
from .models import Cliente, Agendamento               # os models (tabelas) que vamos usar aqui
from .forms import ClienteForm      # os formulários que vamos usar aqui

def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'core/form_cliente.html', {'form': form, 'titulo': 'Novo Cliente'})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('detalhe_cliente', id=cliente.id)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'core/form_cliente.html', {'form': form, 'titulo': 'Editar Cliente'})

# View da LISTA de clientes  →  responde ao endereço /clientes/
def lista_clientes(request):
    clientes = Cliente.objects.all()   # busca TODOS os clientes no banco (retorna uma lista)
    # render() = pega o template + injeta os dados + devolve a página pronta.
    # O dicionário {'clientes': clientes} é o "context": leva os dados pro HTML.
    return render(request, 'core/lista_clientes.html', {'clientes': clientes})


# View de DETALHE de um cliente  →  responde a /clientes/<id>/
# Repara no parâmetro 'id': ele chega da URL (o <int:id> lá no urls.py).
def detalhe_cliente(request, id):
    # get_object_or_404 busca UM cliente pelo id.
    # Se esse id não existir, mostra a página "404 - não encontrado" em vez de quebrar o site.
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'core/detalhe_cliente.html', {'cliente': cliente})


# View da LISTA de agendamentos  →  responde a /agendamentos/
def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()   # busca todos os agendamentos
    return render(request, 'core/lista_agendamentos.html', {'agendamentos': agendamentos})
