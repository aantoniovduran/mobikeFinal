from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$',views.pagina_principal, name='pagina_principal'),
    url(r'^formulario/',views.pagina_formulario, name='pagina_formulario'),
    url(r'^login/',views.pagina_login, name='pagina_login'),
    url(r'^estacionamiento/',views.pagina_estacionamiento, name='pagina_estacionamiento'),
    url(r'^bicicleta/',views.pagina_bicicleta, name='pagina_bicicleta'),
]