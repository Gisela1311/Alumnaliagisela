from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_alumnalia/', include('app_alumnalia.urls', namespace='alumnalia')),
]

