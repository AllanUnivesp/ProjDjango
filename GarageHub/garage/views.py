# from django.forms import BaseModelForm
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Cliente, Veiculo, Ordem
from .forms import ClientesForm, VeiculosForm, OrdemForm

# from django.contrib.auth.mixins import LoginRequiredMixin

# def get_name(request):
#     print('esta entrando aqui')
#     if request.method == 'POST':
#         form = VeiculosForm(request.POST)
#         if form.is_valid():
#             print('esta entrando aqui1')
            
#             return HttpResponseRedirect('/')
#     else:
#         # form = OrdemForm()
#         form = VeiculosForm()
#         print('esta entrando aqui2')
#     return render(request, 'garage/ordens/name.html', {'form':form})

# def post_list(request):
#     posts = Post.published.all()
#     return render(request, 'garage/post/list.html', {'posts':posts})

# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    
#     return render(request, 'garage/post/detail.html', {'post': post})

def home(request):
    context = {
        'clientes': Ordem.objects.all()
    }
    return render(request, 'garage/home.html', context)


class HomeListView(ListView):
    model = Ordem
    template_name = 'garage/home.html'
    context_object_name = 'ordens'
    ordering = ['-data_criacao']


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
    template_name = 'garage/clientes/client_create_form.html'
    form_class = ClientesForm
    
 
class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = '/garage/clientes'
    template_name = 'garage/clientes/client_confirm_delete.html'
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep']
    template_name = 'garage/clientes/client_update_form.html'

    
class VeiculoListView(ListView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_home.html'
    context_object_name = 'veiculos'
    ordering = ['-data_criacao']
    
class VeiculoDetailView(DetailView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_details.html'
    
class VeiculoCreateView(CreateView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_create_form.html'
    form_class = VeiculosForm
    
    
class VeiculoDeleteView(DeleteView):
    model = Veiculo
    success_url = '/garage/veiculos'
    template_name = 'garage/veiculos/veiculo_confirm_delete.html'
    
class VeiculoUpdateView(UpdateView):
    model = Veiculo
    fields = ['marca','modelo', 'placa', 'motor', 'ano']
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
    template_name = 'garage/ordens/ordem_details.html'


class OrdemCreateView(CreateView):
    model = Ordem
    template_name = 'garage/ordens/ordem_create_form.html'
    form_class = OrdemForm

    
class OrdemDeleteView(DeleteView):
    model = Ordem
    success_url = '/garage/ordens'
    template_name = 'garage/ordens/ordem_confirm_delete.html'
    
class OrdemUpdateView(UpdateView):
    model = Ordem
    form_class = OrdemForm
    template_name = 'garage/ordens/ordem_update_form.html'
    success_url = '/garage/ordens'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)