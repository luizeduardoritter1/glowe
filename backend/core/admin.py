from django.contrib import admin
from .models import Cliente, ItemCatalogo, Agendamento, Evento

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'data_nascimento']
admin.site.register(Cliente, ClienteAdmin)

admin.site.register(ItemCatalogo)

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data_hora', 'status', 'valor_total']
    list_filter = ['status']
    search_fields = ['cliente__nome']
admin.site.register(Agendamento, AgendamentoAdmin)

class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_evento', 'cliente']
admin.site.register(Evento, EventoAdmin)