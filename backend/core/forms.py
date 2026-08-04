from django import forms
from .models import Cliente, Agendamento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email', 'data_nascimento', 'observacoes']

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'evento', 'itens', 'data_hora', 'status', 'observacoes']