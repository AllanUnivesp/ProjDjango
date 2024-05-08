from django.urls import path, include
from .views import (
    # post_detail,
    # post_list,
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
    # get_name
    )

app_name = 'garage'

urlpatterns = [
<<<<<<< HEAD
    path('', HomeListView.as_view(), name='garage-home'),
    path('clientes/', ClienteListView.as_view(), name='client-view'),
=======
    
    # path('', post_list, name='post_list'),
    # path('<int:id>/', post_detail, name='post_detail'),
    # path('nome', get_name, name='garage-nome'),



# construindo a list view do inicio

    path('', HomeListView.as_view(), name='garage-home'),
    path('clientes', ClienteListView.as_view(), name='client-view'),
>>>>>>> parent of 4bdee90 (Refactor templates and apps configuration)
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='client-detail'),
    path('clientes/new/', ClienteCreateView.as_view(), name='client-create'),
    path('clientes/<int:pk>/update/', ClienteUpdateView.as_view(), name='client-update'),
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='client-delete'),
    
<<<<<<< HEAD
    path('veiculos/', VeiculoListView.as_view(), name='veiculo-view'),
=======
    path('veiculos', VeiculoListView.as_view(), name='veiculo-view'),
>>>>>>> parent of 4bdee90 (Refactor templates and apps configuration)
    path('veiculos/<int:pk>/', VeiculoDetailView.as_view(), name='veiculo-detail'),
    path('veiculos/new/', VeiculoCreateView.as_view(), name='veiculo-create'),
    path('veiculos/<int:pk>/update/', VeiculoUpdateView.as_view(), name='veiculo-update'),
    path('veiculos/<int:pk>/delete/', VeiculoDeleteView.as_view(), name='veiculo-delete'),
    
<<<<<<< HEAD
    path('ordens/', OrdemListView.as_view(), name='ordem-view'),
    path('ordens/<int:pk>/', OrdemDetailView.as_view(), name='ordem-detail'),
    path('ordens/new/', OrdemCreateView.as_view(), name='ordem-create'),
=======
    path('ordens', OrdemListView.as_view(), name='ordem-view'),
    
    path('ordens/<int:pk>/', OrdemDetailView.as_view(), name='ordem-detail'),
    
    
    path('ordens/new/', OrdemCreateView.as_view(), name='ordem-create'),
    
>>>>>>> parent of 4bdee90 (Refactor templates and apps configuration)
    path('ordens/<int:pk>/update/', OrdemUpdateView.as_view(), name='ordem-update'),
    
    
    path('ordens/<int:pk>/delete/', OrdemDeleteView.as_view(), name='ordem-delete'),
<<<<<<< HEAD

    path('admin/', include('grappelli.urls')),
]
=======
    
    
  
]
>>>>>>> parent of 4bdee90 (Refactor templates and apps configuration)
