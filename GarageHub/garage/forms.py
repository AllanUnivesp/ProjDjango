from django import forms
from django.forms import ModelForm
from .models import Veiculo, Cliente



class OrdemForm(forms.Form):
    
    marca = forms.CharField(label='Marca', max_length=100)
    modelo = forms.CharField(label='Modelo', max_length=100)
    ano = forms.CharField(label='Ano', max_length=100)
    

class VeiculosForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca','modelo', 'placa', 'motor', 'ano', ]

        
class ClientesForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep', ]
