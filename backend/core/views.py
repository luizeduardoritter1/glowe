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
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from datetime import date, timedelta
from django.db.models import Sum

from .models import Cliente, Agendamento, ItemCatalogo, Evento, Lancamento, ItemOrcamento
from .forms import ClienteForm, AgendamentoForm, ItemCatalogoForm, EventoForm, LancamentoForm, ItemOrcamentoForm


# Mixins de feedback — mostram uma mensagem de sucesso após salvar/excluir.
class MensagemSalvarMixin(SuccessMessageMixin):
    success_message = 'Salvo com sucesso! ✅'


class MensagemExcluirMixin:
    def form_valid(self, form):
        resposta = super().form_valid(form)
        messages.success(self.request, 'Excluído com sucesso.')
        return resposta


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


class ClienteCreateView(LoginRequiredMixin, MensagemSalvarMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/form.html'
    extra_context = {'titulo': 'Novo Cliente'}


class ClienteUpdateView(LoginRequiredMixin, MensagemSalvarMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/form.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Cliente'}


class ClienteDeleteView(LoginRequiredMixin, MensagemExcluirMixin, DeleteView):
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


class AgendamentoCreateView(LoginRequiredMixin, MensagemSalvarMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'core/form.html'
    extra_context = {'titulo': 'Novo Agendamento'}


class AgendamentoUpdateView(LoginRequiredMixin, MensagemSalvarMixin, UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'core/form.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Agendamento'}


class AgendamentoDeleteView(LoginRequiredMixin, MensagemExcluirMixin, DeleteView):
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


class ItemCatalogoCreateView(LoginRequiredMixin, MensagemSalvarMixin, CreateView):
    model = ItemCatalogo
    form_class = ItemCatalogoForm
    template_name = 'core/form.html'
    extra_context = {'titulo': 'Novo Item'}


class ItemCatalogoUpdateView(LoginRequiredMixin, MensagemSalvarMixin, UpdateView):
    model = ItemCatalogo
    form_class = ItemCatalogoForm
    template_name = 'core/form.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Item'}


class ItemCatalogoDeleteView(LoginRequiredMixin, MensagemExcluirMixin, DeleteView):
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


class EventoCreateView(LoginRequiredMixin, MensagemSalvarMixin, CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'core/form.html'
    extra_context = {'titulo': 'Novo Evento'}


class EventoUpdateView(LoginRequiredMixin, MensagemSalvarMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'core/form.html'
    pk_url_kwarg = 'id'
    extra_context = {'titulo': 'Editar Evento'}


class EventoDeleteView(LoginRequiredMixin, MensagemExcluirMixin, DeleteView):
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


# ═══════════════ FINANCEIRO ═══════════════

@login_required
def financeiro(request):
    hoje = date.today()
    do_mes = Lancamento.objects.filter(data__year=hoje.year, data__month=hoje.month)

    def total(tipo):
        return do_mes.filter(tipo=tipo).aggregate(t=Sum('valor'))['t'] or 0

    receitas = total(Lancamento.Tipo.RECEITA)
    despesas = total(Lancamento.Tipo.DESPESA)

    contexto = {
        'mes': hoje,
        'receitas': receitas,
        'despesas': despesas,
        'lucro': receitas - despesas,
        'recentes': Lancamento.objects.all()[:8],
    }
    return render(request, 'core/financeiro.html', contexto)


class LancamentoCreateView(LoginRequiredMixin, MensagemSalvarMixin, CreateView):
    model = Lancamento
    form_class = LancamentoForm
    template_name = 'core/form.html'
    extra_context = {'titulo': 'Novo Lançamento'}


class LancamentoDeleteView(LoginRequiredMixin, MensagemExcluirMixin, DeleteView):
    model = Lancamento
    template_name = 'core/confirmar_exclusao.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('financeiro')


# ═══════════════ ORÇAMENTO (itens de linha + página pública) ═══════════════

@login_required
def adicionar_item_orcamento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        form = ItemOrcamentoForm(request.POST)
        if form.is_valid():
            linha = form.save(commit=False)   # não salva ainda — falta o evento
            linha.evento = evento             # vincula ao evento da URL
            linha.save()
            return redirect('detalhe_evento', id=evento.id)
    else:
        form = ItemOrcamentoForm()
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Adicionar item ao orçamento'})


@login_required
def remover_item_orcamento(request, id):
    linha = get_object_or_404(ItemOrcamento, id=id)
    evento_id = linha.evento.id
    if request.method == 'POST':      # remoção só via POST (segurança)
        linha.delete()
    return redirect('detalhe_evento', id=evento_id)


def orcamento_publico(request, token):
    # Página PÚBLICA (sem login) — a cliente abre pelo link com o token único.
    evento = get_object_or_404(Evento, token=token)
    return render(request, 'core/orcamento_publico.html', {'evento': evento})
