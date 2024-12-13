from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, get_resolver

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('app_alumnalia/', include('app_alumnalia.urls', namespace='app_alumnalia')),
]


print(f" control --> {get_resolver().reverse_dict.keys()} <")
