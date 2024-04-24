from django.urls import path
from .views import (
    ClienteListView,
    ClienteDetailView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    VeiculoListView,
    VeiculoDetailView,
    VeiculoCreateView,
    VeiculoDeleteView,
    VeiculoUpdateView,
    OrdemCreateView,
    OrdemDeleteView,
    OrdemDetailView,
    OrdemListView,
    OrdemUpdateView,
    HomeListView,
)

app_name = 'garage'

urlpatterns = [
    # Página inicial
    path('', HomeListView.as_view(), name='garage-home'),

    # URLs relacionadas aos clientes
    path('clientes/', ClienteListView.as_view(), name='client-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='client-detail'),
    path('clientes/new/', ClienteCreateView.as_view(), name='client-create'),
    path('clientes/<int:pk>/update/', ClienteUpdateView.as_view(), name='client-update'),
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='client-delete'),

    # URLs relacionadas aos veículos
    path('veiculos/', VeiculoListView.as_view(), name='veiculo-list'),
    path('veiculos/<int:pk>/', VeiculoDetailView.as_view(), name='veiculo-detail'),
    path('veiculos/new/', VeiculoCreateView.as_view(), name='veiculo-create'),
    path('veiculos/<int:pk>/update/', VeiculoUpdateView.as_view(), name='veiculo-update'),
    path('veiculos/<int:pk>/delete/', VeiculoDeleteView.as_view(), name='veiculo-delete'),

    # URLs relacionadas às ordens de serviço
    path('ordens/', OrdemListView.as_view(), name='ordem-list'),
    path('ordens/new/', OrdemCreateView.as_view(), name='ordem-create'),
    path('ordens/<int:pk>/', OrdemDetailView.as_view(), name='ordem-detail'),
    path('ordens/<int:pk>/update/', OrdemUpdateView.as_view(), name='ordem-update'),
    path('ordens/<int:pk>/delete/', OrdemDeleteView.as_view(), name='ordem-delete'),
]
