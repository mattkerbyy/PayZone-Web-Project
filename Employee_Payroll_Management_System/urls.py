from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from PayZone.views import user_login, user_register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('PayZone.urls')),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
