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

class GarageBaseView:
    model = None
    template_name = None
    context_object_name = None
    form_class = None
    success_url = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('garage:login')
        return super().dispatch(request, *args, **kwargs)

class HomeListView(GarageBaseView, ListView):
    model = Ordem
    template_name = 'garage/home.html'
    context_object_name = 'ordens'
    ordering = ['-data_criacao']

class ClienteListView(GarageBaseView, ListView):
    model = Cliente
    template_name = 'garage/clientes/client_home.html'
    context_object_name = 'clientes'
    ordering = ['-data_criacao']

class ClienteDetailView(GarageBaseView, DetailView):
    model = Cliente
    template_name = 'garage/clientes/client_details.html'

class ClienteCreateView(GarageBaseView, CreateView):
    model = Cliente
    template_name = 'garage/clientes/client_create_form.html'
    form_class = ClientesForm
    success_url = reverse_lazy('garage:client-list')


class ClienteDeleteView(GarageBaseView, DeleteView):
    model = Cliente
    success_url = reverse_lazy('garage:client-list')
    template_name = 'garage/clientes/client_confirm_delete.html'
    form_class = ClientesForm  # Verifique se esta linha está definindo a classe do formulário corretamente

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('garage:login')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        cliente = self.get_object()
        cliente.delete()
        return redirect(self.success_url)


class ClienteUpdateView(GarageBaseView, UpdateView):
    model = Cliente
    fields = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep']
    template_name = 'garage/clientes/client_update_form.html'
    success_url = reverse_lazy('garage:client-list')

class VeiculoListView(GarageBaseView, ListView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_home.html'
    context_object_name = 'veiculos'
    ordering = ['-data_criacao']

class VeiculoDetailView(GarageBaseView, DetailView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_details.html'

class VeiculoCreateView(GarageBaseView, CreateView):
    model = Veiculo
    template_name = 'garage/veiculos/veiculo_create_form.html'
    form_class = VeiculosForm
    success_url = reverse_lazy('garage:veiculo-list')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user  
        return super().form_valid(form)



class VeiculoDeleteView(GarageBaseView, DeleteView):
    model = Veiculo
    success_url = reverse_lazy('garage:veiculo-list')
    template_name = 'garage/veiculos/veiculo_confirm_delete.html'
    form_class = VeiculosForm  # Adicionando o formulário correto

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('garage:login')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Obter o objeto Veiculo a ser excluído
        veiculo = self.get_object()

        # Executar a exclusão
        veiculo.delete()

        # Redirecionar para a página de sucesso após a exclusão
        return redirect(self.success_url)



class VeiculoUpdateView(GarageBaseView, UpdateView):
    model = Veiculo
    fields = ['marca','modelo', 'placa', 'motor', 'ano']
    template_name = 'garage/veiculos/veiculo_update_form.html'
    success_url = reverse_lazy('garage:veiculo-list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class OrdemBaseView(GarageBaseView, ListView):
    template_name = 'garage/ordens/ordem_home.html'
    context_object_name = 'ordens'
    ordering = ['-cliente_id']

class OrdemDetailView(GarageBaseView, DetailView):
    model = Ordem
    template_name = 'garage/ordens/ordem_details.html'

class OrdemCreateView(GarageBaseView, CreateView):
    model = Ordem
    template_name = 'garage/ordens/ordem_create_form.html'
    form_class = OrdemForm
    success_url = reverse_lazy('garage:ordem-list')

    def form_valid(self, form):
        form.instance.autor = self.request.user  
        return super().form_valid(form)


class OrdemDeleteView(DeleteView):
    model = Ordem
    success_url = reverse_lazy('garage:ordem-list')
    template_name = 'garage/ordens/ordem_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        # Obter o objeto Ordem a ser excluído
        ordem = self.get_object()

        # Executar a exclusão
        ordem.delete()

        # Redirecionar para a página de sucesso após a exclusão
        return redirect(self.success_url)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('garage:login')
        return super().dispatch(request, *args, **kwargs)


class OrdemUpdateView(GarageBaseView, UpdateView):
    model = Ordem
    form_class = OrdemForm
    template_name = 'garage/ordens/ordem_update_form.html'
    success_url = reverse_lazy('garage:ordem-list')

class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
    success_url = reverse_lazy('garage:home')


class OrdemListView(OrdemBaseView):
    model = Ordem
    template_name = 'garage/ordens/ordem_home.html'
    context_object_name = 'ordens'
    ordering = ['-cliente_id']

    def get_queryset(self):
        return Ordem.objects.all()
