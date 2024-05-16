from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.views import LoginView
from .models import Cliente, Veiculo, Ordem
from .forms import ClientesForm, VeiculosForm, OrdemForm

class HomeListView(ListView):
    model = Ordem
    template_name = 'garage/home.html'
    context_object_name = 'ordens'
    ordering = ['-data_criacao']

    def dispatch(self, request, *args, **kwargs):
        # Verifica se o usuário está autenticado, se não, redireciona para a página de login
        if not request.user.is_authenticated:
            return redirect('garage:login')
        return super().dispatch(request, *args, **kwargs)

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
    success_url = reverse_lazy('garage:client-list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('garage:client-list')
    template_name = 'garage/clientes/client_confirm_delete.html'

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep']
    template_name = 'garage/clientes/client_update_form.html'
    success_url = reverse_lazy('garage:client-list')

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
    success_url = reverse_lazy('garage:veiculo-list')

class VeiculoDeleteView(DeleteView):
    model = Veiculo
    success_url = reverse_lazy('garage:veiculo-list')
    template_name = 'garage/veiculos/veiculo_confirm_delete.html'

class VeiculoUpdateView(UpdateView):
    model = Veiculo
    fields = ['marca','modelo', 'placa', 'motor', 'ano']
    template_name = 'garage/veiculos/veiculo_update_form.html'
    success_url = reverse_lazy('garage:veiculo-list')
    
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
    success_url = reverse_lazy('garage:ordem-list')

class OrdemDeleteView(DeleteView):
    model = Ordem
    success_url = reverse_lazy('garage:ordem-list')
    template_name = 'garage/ordens/ordem_confirm_delete.html'

class OrdemUpdateView(UpdateView):
    model = Ordem
    form_class = OrdemForm
    template_name = 'garage/ordens/ordem_update_form.html'
    success_url = reverse_lazy('garage:ordem-list')

class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    success_url = reverse_lazy('garage:home')  # Redireciona para a página inicial após o login
