from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Post, Cliente, Veiculo, Ordem

def home(request):
    context = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'garage/home.html', context)

class ClienteListView(ListView):
    model = Cliente
    template_name = 'garage/clientes/client_home.html'
    context_object_name = 'clientes'
    ordering = ['-data_criacao']
    
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'garage/clientes/client_details.html'
    
class ClienteCreateView(CreateView):
    model = Cliente
    # fields = vars(Cliente).keys() #para pegar a lista direto do modelo em models.py
    fields = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep', 'data_criacao', 'email']
    template_name = 'garage/clientes/client_create_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = '/garage/clientes'
    template_name = 'garage/clientes/client_confirm_delete.html'
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep', 'data_criacao']
    template_name = 'garage/clientes/client_update_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
 

def post_list(request):
    posts = Post.published.all()
    return render(request, 'garage/post/list.html', {'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    
    return render(request, 'garage/post/detail.html', {'post': post})

class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_inicio.html'
    context_object_name = 'veiculos'
    ordering = ['-data_criacao']
    
class VeiculoDetailView(DetailView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_details.html'
    
class VeiculoCreateView(CreateView):
    model = Veiculo
    fields = ['marca','modelo', 'placa', 'motor', 'ano', 'data_criacao']
    template_name = 'garage/veiculos/veiculo_create_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class VeiculoDeleteView(DeleteView):
    model = Veiculo
    success_url = '/garage/veiculos'
    template_name = 'garage/veiculos/veiculo_confirm_delete.html'
    
class VeiculoUpdateView(UpdateView):
    model = Veiculo
    fields = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep', 'data_criacao']
    template_name = 'garage/veiculos/veiculo_update_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class OrdemListView(ListView):
    model = Ordem
    template_name = 'garage/ordens/ordem_home.html'
    context_object_name = 'ordens'
    ordering = ['-cliente_id']
    
class OrdemDetailView(DetailView):
    model = Ordem
    template_name = 'garage/ordems/ordem_details.html'
    
class OrdemCreateView(CreateView):
    model = Ordem
    fields = ['titulo', 'status', 'condicao', 'descricao', 'diagnostico', 'data_ordem', 'veiculo_id', 'cliente_id']
    template_name = 'garage/ordems/ordem_create_form.html'
    
    
    
    
    
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class OrdemDeleteView(DeleteView):
    model = Ordem
    success_url = '/garage/ordems'
    template_name = 'garage/ordems/ordem_confirm_delete.html'
    
class OrdemUpdateView(UpdateView):
    model = Ordem
    fields = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep', 'data_criacao']
    template_name = 'garage/ordems/ordem_update_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)