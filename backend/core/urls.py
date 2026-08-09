# urls.py — o "mapa de endereços" do app core.
# Agora as rotas apontam para Views Baseadas em Classe (CBV), com .as_view().
# Os NOMES (name=) foram mantidos, então os {% url %} dos templates continuam iguais.

from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # ---- Autenticação / home ----
    path('', RedirectView.as_view(pattern_name='lista_agendamentos'), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ---- Clientes ----
    path('clientes/', views.ClienteListView.as_view(), name='lista_clientes'),
    path('clientes/novo/', views.ClienteCreateView.as_view(), name='novo_cliente'),
    path('clientes/<int:id>/editar/', views.ClienteUpdateView.as_view(), name='editar_cliente'),
    path('clientes/<int:id>/excluir/', views.ClienteDeleteView.as_view(), name='excluir_cliente'),
    path('clientes/<int:id>/', views.ClienteDetailView.as_view(), name='detalhe_cliente'),

    # ---- Agenda (calendário semanal) ----
    path('agenda/', views.agenda, name='agenda'),

    # ---- Agendamentos ----
    path('agendamentos/', views.AgendamentoListView.as_view(), name='lista_agendamentos'),
    path('agendamentos/novo/', views.AgendamentoCreateView.as_view(), name='novo_agendamento'),
    path('agendamentos/<int:id>/editar/', views.AgendamentoUpdateView.as_view(), name='editar_agendamento'),
    path('agendamentos/<int:id>/excluir/', views.AgendamentoDeleteView.as_view(), name='excluir_agendamento'),
    path('agendamentos/<int:id>/', views.AgendamentoDetailView.as_view(), name='detalhe_agendamento'),

    # ---- Catálogo ----
    path('catalogo/', views.ItemCatalogoListView.as_view(), name='lista_catalogo'),
    path('catalogo/novo/', views.ItemCatalogoCreateView.as_view(), name='novo_item'),
    path('catalogo/<int:id>/editar/', views.ItemCatalogoUpdateView.as_view(), name='editar_item'),
    path('catalogo/<int:id>/excluir/', views.ItemCatalogoDeleteView.as_view(), name='excluir_item'),
    path('catalogo/<int:id>/', views.ItemCatalogoDetailView.as_view(), name='detalhe_item'),

    # ---- Eventos ----
    path('eventos/', views.EventoListView.as_view(), name='lista_eventos'),
    path('eventos/novo/', views.EventoCreateView.as_view(), name='novo_evento'),
    path('eventos/<int:id>/editar/', views.EventoUpdateView.as_view(), name='editar_evento'),
    path('eventos/<int:id>/excluir/', views.EventoDeleteView.as_view(), name='excluir_evento'),
    path('eventos/<int:id>/', views.EventoDetailView.as_view(), name='detalhe_evento'),

    # ---- Financeiro ----
    path('financeiro/', views.financeiro, name='financeiro'),
    path('financeiro/novo/', views.LancamentoCreateView.as_view(), name='novo_lancamento'),
    path('financeiro/<int:id>/excluir/', views.LancamentoDeleteView.as_view(), name='excluir_lancamento'),
]
