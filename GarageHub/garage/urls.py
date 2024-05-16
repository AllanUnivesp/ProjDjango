from django.urls import path, include
from django.contrib.auth.views import LogoutView
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
    CustomLoginView,
)

app_name = 'garage'

urlpatterns = [
    # Authentication URLs
    path('', CustomLoginView.as_view(), name='login'),
    path('home/', HomeListView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(next_page='garage:home'), name='logout'),

    # Cliente URLs
    path('clientes/', ClienteListView.as_view(), name='client-list'),
    path('clientes/new/', ClienteCreateView.as_view(), name='client-create'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='client-detail'),
    path('clientes/<int:pk>/update/', ClienteUpdateView.as_view(), name='client-update'),
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='client-delete'),

    # Veiculo URLs
    path('veiculos/', VeiculoListView.as_view(), name='veiculo-list'),
    path('veiculos/new/', VeiculoCreateView.as_view(), name='veiculo-create'),
    path('veiculos/<int:pk>/', VeiculoDetailView.as_view(), name='veiculo-detail'),
    path('veiculos/<int:pk>/update/', VeiculoUpdateView.as_view(), name='veiculo-update'),
    path('veiculos/<int:pk>/delete/', VeiculoDeleteView.as_view(), name='veiculo-delete'),

    # Ordem URLs
    path('ordens/', OrdemListView.as_view(), name='ordem-list'),
    path('ordens/new/', OrdemCreateView.as_view(), name='ordem-create'),
    path('ordens/<int:pk>/', OrdemDetailView.as_view(), name='ordem-detail'),
    path('ordens/<int:pk>/update/', OrdemUpdateView.as_view(), name='ordem-update'),
    path('ordens/<int:pk>/delete/', OrdemDeleteView.as_view(), name='ordem-delete'),
   


    # Admin URLs
    path('admin/', include('grappelli.urls')),
]
