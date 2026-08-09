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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import date, timedelta

from .models import Cliente, Agendamento, ItemCatalogo, Evento
from .forms import ClienteForm, AgendamentoForm, ItemCatalogoForm, EventoForm


# ═══════════════ CLIENTE ═══════════════

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'core/lista_clientes.html'
    context_object_name = 'clientes'


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'core/detalhe_cliente.html'
    context_object_name = 'cliente'
    pk_url_kwarg = 'id'


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/form.html'
    extra_context = {'titulo': 'Novo Cliente'}


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/form.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Cliente'}


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'core/confirmar_exclusao.html'
    context_object_name = 'cliente'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('lista_clientes')


# ═══════════════ AGENDAMENTO ═══════════════

class AgendamentoListView(LoginRequiredMixin, ListView):
    model = Agendamento
    template_name = 'core/lista_agendamentos.html'
    context_object_name = 'agendamentos'


class AgendamentoDetailView(LoginRequiredMixin, DetailView):
    model = Agendamento
    template_name = 'core/detalhe_agendamento.html'
    context_object_name = 'agendamento'
    pk_url_kwarg = 'id'


class AgendamentoCreateView(LoginRequiredMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'core/form.html'
    extra_context = {'titulo': 'Novo Agendamento'}


class AgendamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'core/form.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Agendamento'}


class AgendamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Agendamento
    template_name = 'core/confirmar_exclusao.html'
    context_object_name = 'agendamento'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('lista_agendamentos')


# ═══════════════ CATÁLOGO (ItemCatalogo) ═══════════════

class ItemCatalogoListView(LoginRequiredMixin, ListView):
    model = ItemCatalogo
    template_name = 'core/lista_catalogo.html'
    context_object_name = 'itens'


class ItemCatalogoDetailView(LoginRequiredMixin, DetailView):
    model = ItemCatalogo
    template_name = 'core/detalhe_item.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'


class ItemCatalogoCreateView(LoginRequiredMixin, CreateView):
    model = ItemCatalogo
    form_class = ItemCatalogoForm
    template_name = 'core/form.html'
    extra_context = {'titulo': 'Novo Item'}


class ItemCatalogoUpdateView(LoginRequiredMixin, UpdateView):
    model = ItemCatalogo
    form_class = ItemCatalogoForm
    template_name = 'core/form.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Item'}


class ItemCatalogoDeleteView(LoginRequiredMixin, DeleteView):
    model = ItemCatalogo
    template_name = 'core/confirmar_exclusao.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('lista_catalogo')


# ═══════════════ EVENTO ═══════════════

class EventoListView(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'core/lista_eventos.html'
    context_object_name = 'eventos'


class EventoDetailView(LoginRequiredMixin, DetailView):
    model = Evento
    template_name = 'core/detalhe_evento.html'
    context_object_name = 'evento'
    pk_url_kwarg = 'id'


class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'core/form.html'
    extra_context = {'titulo': 'Novo Evento'}


class EventoUpdateView(LoginRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'core/form.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Evento'}


class EventoDeleteView(LoginRequiredMixin, DeleteView):
    model = Evento
    template_name = 'core/confirmar_exclusao.html'
    context_object_name = 'evento'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('lista_eventos')


# ═══════════════ AGENDA (calendário semanal) ═══════════════

@login_required
def agenda(request):
    # 'semana' é um deslocamento em semanas: 0 = atual, -1 = anterior, 1 = próxima.
    try:
        off = int(request.GET.get('semana', 0))
    except (TypeError, ValueError):
        off = 0

    hoje = date.today()
    # segunda-feira da semana escolhida (weekday(): segunda=0 ... domingo=6)
    inicio = hoje - timedelta(days=hoje.weekday()) + timedelta(weeks=off)

    dias = []
    for i in range(7):
        d = inicio + timedelta(days=i)
        dias.append({
            'data': d,
            'agendamentos': Agendamento.objects.filter(data_hora__date=d).order_by('data_hora'),
            'hoje': d == hoje,
        })

    contexto = {
        'dias': dias,
        'inicio': inicio,
        'fim': inicio + timedelta(days=6),
        'ant': off - 1,
        'prox': off + 1,
    }
    return render(request, 'core/agenda.html', contexto)
