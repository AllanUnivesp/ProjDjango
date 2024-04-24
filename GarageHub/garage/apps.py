from django.apps import AppConfig

class GarageConfig(AppConfig):
    # Define o tipo de campo de chave primária automática para os modelos deste aplicativo
    default_auto_field = 'django.db.models.BigAutoField'

    # Define o nome do aplicativo Django
    name = 'garage'
