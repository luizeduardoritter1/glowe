# urls.py — o "mapa de endereços" do app core.
# Aqui a gente diz: "quando alguém acessar TAL endereço, chame TAL view".

from django.urls import path   # 'path' cria uma rota (liga um endereço a uma view)
from . import views            # importa as views deste mesmo app (o "." significa "aqui, nesta pasta")

# Lista de rotas do app. O Django lê de cima pra baixo e usa a primeira que casar.
urlpatterns = [
    # Endereço /clientes/  →  chama a view lista_clientes
    # O name='lista_clientes' é o "apelido" da rota, usado no template com {% url 'lista_clientes' %}
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/novo/', views.novo_cliente, name='novo_cliente'),
    path('clientes/<int:id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('clientes/<int:id>/excluir/', views.excluir_cliente, name='excluir_cliente'),

    # Endereço /clientes/<numero>/  →  chama a view detalhe_cliente
    # <int:id> captura um número da URL e entrega pra view no parâmetro 'id'.
    # Ex: acessar /clientes/1/  faz  id = 1
    path('clientes/<int:id>/', views.detalhe_cliente, name='detalhe_cliente'),

    # Endereço /agendamentos/  →  chama a view lista_agendamentos
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos'),
    path('agendamentos/novo/', views.novo_agendamento, name='novo_agendamento'),
]
