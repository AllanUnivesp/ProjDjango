from django.forms import ModelForm
from .models import Veiculo, Cliente, Ordem
# from django.utils.translation import gettext_lazy as _



# iniciando a implementacao do ModelForm para ter mais controle sob os formularios


class OrdemForm(ModelForm):
    class Meta:
        model = Ordem
        fields = ['titulo', 'status', 'condicao', 'descricao', 'diagnostico', 'observacoes', 'veiculo_id', 'cliente_id']
        labels = {'titulo': 'Título',
                  'condicao': 'Condição',
                  'descricao': 'Descrição',
                  'diagnostico': 'Diagnóstico',
                  'observacoes': 'Observações',
                  'veiculo_id': 'Veículo',
                  'cliente_id': 'Cliente'
                  }


class VeiculosForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca','modelo', 'placa', 'motor', 'ano']

        
class ClientesForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'autor','n_cpf', 'endereco', 'bairro', 'cidade', 'cep', 'email']
        labels = {'endereco': 'Endereço',
                  'n_cpf': 'Número do CPF',
                  'cep': 'CEP'}
