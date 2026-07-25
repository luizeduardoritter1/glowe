from django.contrib import admin
from .models import Cliente, ItemCatalogo, Agendamento

admin.site.register(Cliente)
admin.site.register(ItemCatalogo)
admin.site.register(Agendamento)