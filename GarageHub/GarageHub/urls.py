from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    # Admin URLs
    path('admin/', admin.site.urls),
    
    # URLs para registro de usuários
    path('register/', user_views.register, name='register'),
    
    # URLs para o aplicativo 'garage'
    path('garage/', include('garage.urls', namespace='garage')),
    
    # URLs para a página inicial
    path('', include('garage.urls', namespace='paginicial')),
]

# Servir arquivos de mídia estática durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
