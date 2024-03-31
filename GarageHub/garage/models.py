from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    n_cpf = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    data_criacao = models.DateField()
    email = models.CharField(max_length=100)
    
        
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('garage:client-detail', args=[self.id])
    
class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=250)
    motor = models.CharField(max_length=150)
    ano = models.CharField(max_length=50)
    data_criacao = models.DateField()
    
    def __str__(self):
        return self.modelo

    def get_absolute_url(self):
        return reverse('garage:veiculo-detail', args=[self.id])

class Ordem(models.Model):

    CONDICOES_VEICULO = (
        ("A", "Normal - Proprietário veio rodando"),
        ("B", "Sem funcionar - veio no guincho"),
        ("C", "Com anomalia - Proprietário veio rodando"),
        ("D", "Com anomalia - Veio rodando por terceiro")
    )
    STATUS_ORDEM = (
        ('A', 'Em Execução - aprovado pelo cliente'),
        ('B', 'Em Aberto -  aguardando aprovação pelo cliente'),
        ('C', 'Em Aberto -  aguardando peças'),
        ('D', 'Finallizado'),
        ('E', 'Finallizado - interrompido pelo cliente')
    )
    
    titulo = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_ORDEM,default='Em Execução - aprovado pelo cliente', max_length=100)
    condicao = models.CharField(choices=CONDICOES_VEICULO,default='Normal - Proprietário veio rodando', max_length=100)
    descricao = models.CharField(max_length=150)
    diagnostico = models.CharField(max_length=150, default='Descreva o problema observado')
    data_ordem = models.DateField()
    veiculo_id = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('garage:ordem-detail', args=[self.id])

class CadastroPecas(models.Model):
    nome = models.CharField(max_length=150, default='sem nome')
    codigo = models.CharField(max_length=50) 
    grupo = models.CharField(max_length=50)    
    subgrupo = models.CharField(max_length=50)     
    fabricante = models.CharField(max_length=50)     
    
    def get_absolute_url(self): 
        return reverse('garage:cadastro-detail', args=[self.id])
    
    
class PecasServico(models.Model):
    peca_id = models.ForeignKey(CadastroPecas, on_delete=models.CASCADE)
    ordem_id = models.ForeignKey(Ordem, on_delete=models.CASCADE)
    

    def get_absolute_url(self):
        return reverse('garage:ordem-detail', args=[self.id])






class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='garage_post',
                               )
      
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    
    def __str__(self):
        return self.title
    
    