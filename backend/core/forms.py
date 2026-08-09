from django import forms
from .models import Cliente, Agendamento, ItemCatalogo, Evento, Lancamento, ItemOrcamento


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'data_nascimento', 'tags', 'observacoes']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_nascimento'].input_formats = ['%Y-%m-%d']


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'evento', 'itens', 'data_hora', 'local', 'endereco', 'status', 'observacoes']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_hora'].input_formats = ['%Y-%m-%dT%H:%M']


class ItemCatalogoForm(forms.ModelForm):
    class Meta:
        model = ItemCatalogo
        fields = ['nome', 'tipo', 'preco', 'custo', 'duracao_min', 'ocupa_agenda']


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'tipo', 'cliente', 'data_evento', 'local', 'valor_sinal', 'observacoes']
        widgets = {
            'data_evento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_evento'].input_formats = ['%Y-%m-%d']


class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = ['descricao', 'tipo', 'valor', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].input_formats = ['%Y-%m-%d']


class ItemOrcamentoForm(forms.ModelForm):
    class Meta:
        model = ItemOrcamento
        fields = ['item', 'quantidade']
