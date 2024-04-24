from django.contrib import admin
from .models import Post, Cliente, Veiculo, CadastroPecas, Ordem

# Registrando o modelo 'Post' no Django Admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na lista de registros
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # Filtros para os registros
    list_filter = ['status', 'created', 'publish', 'author']
    # Campos de pesquisa
    search_fields = ['title', 'body']
    # Campos preenchidos automaticamente
    prepopulated_fields = {'slug': ('title',)}
    # Campos de chave estrangeira substituídos por busca
    raw_id_fields = ['author']
    # Barra de navegação por datas
    date_hierarchy = 'publish'
    # Ordenação padrão dos registros
    ordering = ['status', 'publish']

# Registrando o modelo 'Cliente' no Django Admin
@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ['nome', 'n_cpf', 'endereco', 'bairro', 'cidade', 'cep', 'data_criacao', 'email']
    prepopulated_fields = {'slug': ('nome',)}

# Registrando o modelo 'Veiculo' no Django Admin
@admin.register(Veiculo)
class VeiculosAdmin(admin.ModelAdmin):
    list_display = ['slug', 'marca', 'modelo', 'motor', 'ano', 'data_criacao', 'id']
    prepopulated_fields = {'slug': ('marca', 'placa')}

# Registrando o modelo 'CadastroPecas' no Django Admin
@admin.register(CadastroPecas)
class CadastroPecasAdmin(admin.ModelAdmin):
    list_display = ['nome', 'codigo', 'grupo', 'subgrupo', 'fabricante']
    prepopulated_fields = {'slug': ('nome',)}

# Registrando o modelo 'Ordem' no Django Admin
@admin.register(Ordem)
class OrdemAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'status', 'condicao', 'descricao', 'diagnostico', 'data_criacao', 'cliente_id']
    prepopulated_fields = {'slug': ('titulo',)}
