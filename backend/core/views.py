# views.py — Views Baseadas em Classe (Class-Based Views / CBV).
#
# As "generic views" do Django já trazem o CRUD pronto:
#   ListView   → lista        DetailView → detalhe
#   CreateView → criar         UpdateView → editar        DeleteView → excluir
# A gente só CONFIGURA (qual model, qual template, etc.) — o Django cuida do resto
# (buscar do banco, validar o form, salvar, redirecionar). Muito menos código repetido.
#
# Convenções usadas aqui:
# - template_name → reaproveita os templates que já existiam.
# - context_object_name → o nome da variável no template (ex: 'cliente', 'clientes').
# - pk_url_kwarg = 'id' → nossas rotas usam <int:id> (o padrão do Django seria <int:pk>).
# - Create/Update redirecionam para o get_absolute_url() do model (definido em models.py).
# - extra_context → passa o 'titulo' para o template de formulário.

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Cliente, Agendamento, ItemCatalogo
from .forms import ClienteForm, AgendamentoForm, ItemCatalogoForm


# ═══════════════ CLIENTE ═══════════════

class ClienteListView(ListView):
    model = Cliente
    template_name = 'core/lista_clientes.html'
    context_object_name = 'clientes'


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'core/detalhe_cliente.html'
    context_object_name = 'cliente'
    pk_url_kwarg = 'id'


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/form_cliente.html'
    extra_context = {'titulo': 'Novo Cliente'}


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/form_cliente.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Cliente'}


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'core/confirmar_exclusao.html'
    context_object_name = 'cliente'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('lista_clientes')


# ═══════════════ AGENDAMENTO ═══════════════

class AgendamentoListView(ListView):
    model = Agendamento
    template_name = 'core/lista_agendamentos.html'
    context_object_name = 'agendamentos'


class AgendamentoDetailView(DetailView):
    model = Agendamento
    template_name = 'core/detalhe_agendamento.html'
    context_object_name = 'agendamento'
    pk_url_kwarg = 'id'


class AgendamentoCreateView(CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'core/form_agendamento.html'
    extra_context = {'titulo': 'Novo Agendamento'}


class AgendamentoUpdateView(UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'core/form_agendamento.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Agendamento'}


class AgendamentoDeleteView(DeleteView):
    model = Agendamento
    template_name = 'core/confirmar_exclusao_agendamento.html'
    context_object_name = 'agendamento'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('lista_agendamentos')


# ═══════════════ CATÁLOGO (ItemCatalogo) ═══════════════

class ItemCatalogoListView(ListView):
    model = ItemCatalogo
    template_name = 'core/lista_catalogo.html'
    context_object_name = 'itens'


class ItemCatalogoDetailView(DetailView):
    model = ItemCatalogo
    template_name = 'core/detalhe_item.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'


class ItemCatalogoCreateView(CreateView):
    model = ItemCatalogo
    form_class = ItemCatalogoForm
    template_name = 'core/form_item.html'
    extra_context = {'titulo': 'Novo Item'}


class ItemCatalogoUpdateView(UpdateView):
    model = ItemCatalogo
    form_class = ItemCatalogoForm
    template_name = 'core/form_item.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Item'}


class ItemCatalogoDeleteView(DeleteView):
    model = ItemCatalogo
    template_name = 'core/confirmar_exclusao_item.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('lista_catalogo')
