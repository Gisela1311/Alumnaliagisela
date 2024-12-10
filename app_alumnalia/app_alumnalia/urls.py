"""
URL configuration for app_alumnalia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'app_alumnalia'

urlpatterns = [
    path('inicio/', views.pagina_inicio, name='inicio'),
    path('formadores_form/', views.nuevo_formador, name='nuevo_formador'),
    # path('estudiantes_form/', views.nuevo_estudiante, name='nuevo_estudiante'),
    # Agrega más rutas aquí según sea necesario
]

