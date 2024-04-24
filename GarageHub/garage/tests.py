from django.test import TestCase
from .models import Cliente

class ClienteModelTestCase(TestCase):
    """Testes para o modelo Cliente."""

    def setUp(self):
        """Configuração inicial para os testes."""
        Cliente.objects.create(
            nome="João",
            n_cpf="12345678901",
            endereco="Rua A",
            bairro="Centro",
            cidade="Cidade",
            cep="12345-678",
            email="joao@example.com"
        )

    def test_cliente_str(self):
        """Testa se o método __str__() retorna o nome do cliente."""
        # Obtém o cliente criado no setUp()
        cliente = Cliente.objects.get(nome="João")
        # Verifica se o método __str__() retorna o nome correto
        self.assertEqual(cliente.__str__(), "João")
