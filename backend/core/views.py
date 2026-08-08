# views.py — as "funções de resposta".
# Cada view recebe um pedido (request) do navegador, busca os dados que precisa
# e devolve uma página pronta.

from django.shortcuts import render, get_object_or_404, redirect  # atalhos úteis do Django
from .models import Cliente, Agendamento, ItemCatalogo               # os models (tabelas) que vamos usar aqui
from .forms import ClienteForm, AgendamentoForm, ItemCatalogoForm      # os formulários que vamos usar aqui

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

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'core/confirmar_exclusao.html', {'cliente': cliente})

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

def novo_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'core/form_agendamento.html', {'form': form, 'titulo': 'Novo Agendamento'})

def editar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('detalhe_agendamento', id=agendamento.id)
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'core/form_agendamento.html', {'form': form, 'titulo': 'Editar Agendamento'})

def excluir_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('lista_agendamentos')
    return render(request, 'core/confirmar_exclusao_agendamento.html', {'agendamento': agendamento})

def detalhe_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    return render(request, 'core/detalhe_agendamento.html', {'agendamento': agendamento})


# ═══════════════ CATÁLOGO (ItemCatalogo) ═══════════════

def lista_catalogo(request):
    itens = ItemCatalogo.objects.all()
    return render(request, 'core/lista_catalogo.html', {'itens': itens})

def detalhe_item(request, id):
    item = get_object_or_404(ItemCatalogo, id=id)
    return render(request, 'core/detalhe_item.html', {'item': item})

def novo_item(request):
    if request.method == 'POST':
        form = ItemCatalogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_catalogo')
    else:
        form = ItemCatalogoForm()
    return render(request, 'core/form_item.html', {'form': form, 'titulo': 'Novo Item'})

def editar_item(request, id):
    item = get_object_or_404(ItemCatalogo, id=id)
    if request.method == 'POST':
        form = ItemCatalogoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('detalhe_item', id=item.id)
    else:
        form = ItemCatalogoForm(instance=item)
    return render(request, 'core/form_item.html', {'form': form, 'titulo': 'Editar Item'})

def excluir_item(request, id):
    item = get_object_or_404(ItemCatalogo, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('lista_catalogo')
    return render(request, 'core/confirmar_exclusao_item.html', {'item': item})