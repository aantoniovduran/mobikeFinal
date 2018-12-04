from django.shortcuts import render, redirect, render_to_response
from .models import Usuario

def pagina_principal(request):
	return render(request, 'webmobike/index.html')

def pagina_login(request):
	return render(request, 'webmobike/login.html')

def pagina_formulario(request):
	form = Usuario()

	if request.method == "POST":

		form.Primer_nombre = request.POST['primernombre']
		form.Segundo_nombre = request.POST['segundonombre']
		form.Apellido_paterno = request.POST['apellidopaterno']
		form.Apellido_materno = request.POST['apellidomaterno']
		form.Rut = request.POST['rut']
		form.Telefono = request.POST['telefono']
		form.Email = request.POST['email']
		form.Direccion = request.POST['direccion']
		form.Comuna_trabajo = request.POST['country']
		form.Nombreusuario = request.POST['nombreusuario']
		form.Contraseña = request.POST['contraseña']
		form.Banco = request.POST['banco']
		form.numerotarjeta = request.POST['numerotarjeta']
		form.save()
		
	return render(request, 'webmobike/formulario.html')

def pagina_estacionamiento(request):
	return render(request, 'webmobike/estacionamiento.html')

def pagina_bicicleta(request):
	return render(request, 'webmobike/bicicleta.html')