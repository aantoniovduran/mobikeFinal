from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pagina.urls')),
]
