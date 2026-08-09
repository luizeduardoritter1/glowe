from django import forms
from .models import Cliente, Agendamento, ItemCatalogo, Evento, Lancamento, ItemOrcamento


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'data_nascimento', 'observacoes']


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'evento', 'itens', 'data_hora', 'status', 'observacoes']


class ItemCatalogoForm(forms.ModelForm):
    class Meta:
        model = ItemCatalogo
        fields = ['nome', 'tipo', 'preco', 'custo', 'duracao_min', 'ocupa_agenda']


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'tipo', 'cliente', 'data_evento', 'local', 'valor_sinal', 'observacoes']


class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = ['descricao', 'tipo', 'valor', 'data']


class ItemOrcamentoForm(forms.ModelForm):
    class Meta:
        model = ItemOrcamento
        fields = ['item', 'quantidade']
