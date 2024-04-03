from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('garage/', include('garage.urls', namespace='garage')),
    path('', include('garage.urls', namespace='paginicial')),
]
