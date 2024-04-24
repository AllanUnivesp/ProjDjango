from django.apps import AppConfig

class UsersConfig(AppConfig):
    # Define o campo automático padrão para modelos neste aplicativo
    default_auto_field = 'django.db.models.BigAutoField'

    # Define o nome do aplicativo como 'users'
    name = 'users'
