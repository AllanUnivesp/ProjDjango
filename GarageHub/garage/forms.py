from django.forms import ModelForm
from .models import Veiculo, Cliente, Ordem


class OrdemForm(ModelForm):
    class Meta:
        model = Ordem
        fields = ['titulo', 'status', 'condicao', 'descricao', 'diagnostico', 'veiculo_id', 'cliente_id'] 
    

class VeiculosForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca','modelo', 'placa', 'motor', 'ano']

        
class ClientesForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep', 'email']
