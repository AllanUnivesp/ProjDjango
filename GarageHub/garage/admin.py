from django.contrib import admin
from .models import Post, Cliente, Veiculo, CadastroPecas, Ordem, PecasServico


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title' ,'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['nome' , 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep', 'data_criacao', 'email']
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Veiculo)
class VeiculosAdmin(admin.ModelAdmin):
    list_display = ['marca','modelo' , 'motor', 'ano', 'data_criacao']
    prepopulated_fields = {'slug': ('marca',)}
    
    
@admin.register(CadastroPecas)
class CadastroPecasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'codigo','grupo', 'subgrupo', 'fabricante']
    prepopulated_fields = {'slug': ('nome',)}
    

@admin.register(Ordem)
class OrdemAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'status', 'condicao', 'descricao', 'diagnostico', 'data_ordem', 'veiculo_id', 'cliente_id']
    prepopulated_fields = {'slug': ('titulo',)}
    