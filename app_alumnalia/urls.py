
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formadores/', include('app_alumnalia.urls', namespace='formadores')),
    path('estudiantes/', include('app_alumnalia.urls', namespace='estudiantes')),
    # Puedes añadir más includes según sea necesario
]
