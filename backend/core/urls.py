from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/<int:id>/', views.detalhe_cliente, name='detalhe_cliente'),
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos')
]