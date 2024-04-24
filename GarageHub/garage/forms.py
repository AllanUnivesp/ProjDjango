from django.forms import ModelForm
from .models import Veiculo, Cliente, Ordem

# Formulário para o modelo Ordem
class OrdemForm(ModelForm):
    class Meta:
        model = Ordem
        # Campos do modelo a serem incluídos no formulário
        fields = ['titulo', 'status', 'condicao', 'descricao', 'diagnostico', 'observacoes', 'veiculo_id', 'cliente_id']
        # Rótulos personalizados para os campos do formulário
        labels = {
            'titulo': 'Título',
            'condicao': 'Condição',
            'descricao': 'Descrição',
            'diagnostico': 'Diagnóstico',
            'observacoes': 'Observações',
            'veiculo_id': 'Veículo',
            'cliente_id': 'Cliente'
        }

# Formulário para o modelo Veiculo
class VeiculosForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'placa', 'motor', 'ano']

# Formulário para o modelo Cliente
class ClientesForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'autor', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep', 'email']
        # Rótulos personalizados para os campos do formulário
        labels = {
            'endereco': 'Endereço',
            'n_cpf': 'Número do CPF',
            'cep': 'CEP'
        }
