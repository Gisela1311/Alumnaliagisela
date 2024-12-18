from django.contrib import admin
from django.urls import path, include,get_resolver
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name= "app_alumnalia"

urlpatterns = [
    path("", views.InicioView.as_view(), name= 'inicio'),
    path("inicio/", views.InicioView.as_view(), name= 'inicio'),
#    path('__debug__/', include('debug_toolbar.urls')),
    path('perfil_usuario/', views.PerfilusuarioView.as_view(), name= 'perfil_usuario'),
    path("datos_personales_estudiantes/", views.datos_personales_estudiantes_view.as_view(), name= 'datos_personales_estudiantes'),
    path("datos_personales_formadores/", views.datos_personales_formadores_view.as_view(), name= 'datos_personales_formadores'),
    path('datos_formador/', views.datos_formador_view.as_view(), name='datos_formador'),
    #path('datos_estudiante/', view., name='datos_estudiante'),
    path("oferta_personalizada/", views.oferta_personalizada.as_view(), name= 'oferta_personalizada'),
    path("iniciarsesion/", views.login_view.as_view(), name= 'iniciarsesion'),
    path('admin/', admin.site.urls),

    #path('eliminar/<int:id>/', views.eliminar_fila, name='eliminar_fila'), # elimina un Dato de Dat_Per
    #path('filas/', views.lista_filas, name='lista_filas'),
]
# print(f" control --> {get_resolver().reverse_dict.keys()} <")
