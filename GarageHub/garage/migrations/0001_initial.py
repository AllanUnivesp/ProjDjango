from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroPecas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='sem nome', max_length=150)),
                ('slug', models.SlugField(max_length=250)),
                ('codigo', models.CharField(max_length=50)),
                ('grupo', models.CharField(max_length=50)),
                ('subgrupo', models.CharField(max_length=50)),
                ('fabricante', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('n_cpf', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=250)),
                ('modelo', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=250)),
                ('motor', models.CharField(max_length=150)),
                ('ano', models.CharField(max_length=50)),
                ('data_criacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=250)),
                ('status', models.CharField(choices=[('A', 'Em Execução - aprovado pelo cliente'), ('B', 'Em Aberto -  aguardando aprovação pelo cliente'), ('C', 'Em Aberto -  aguardando peças'), ('D', 'Finallizado'), ('E', 'Finallizado - interrompido pelo cliente')], default='Em Execução - aprovado pelo cliente', max_length=100)),
                ('condicao', models.CharField(choices=[('A', 'Normal - Proprietário veio rodando'), ('B', 'Sem funcionar - veio no guincho'), ('C', 'Com anomalia - Proprietário veio rodando'), ('D', 'Com anomalia - Veio rodando por terceiro')], default='Normal - Proprietário veio rodando', max_length=100)),
                ('descricao', models.CharField(max_length=150)),
                ('diagnostico', models.CharField(default='Descreva o problema observado', max_length=150)),
                ('data_ordem', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.Cliente')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.Veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='PecasServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.Ordem')),
                ('peca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.CadastroPecas')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='garage_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish'],
                'indexes': [models.Index(fields=['-publish'], name='garage_post_publish_f0fc07_idx')],
            },
        ),
    ]
