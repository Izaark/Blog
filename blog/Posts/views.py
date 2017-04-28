from django.shortcuts import render
from django.http import HttpResponse

def post_create(request):
	return HttpResponse('<h1> crear </h1>')

def post_list(request):
	if request.user.is_authenticated():
		context = {
		'title':'users :D',
		'subtitle':'Welcome'
		}
	else:
		context = {
		'title':'No autorizado'
		}
	return render(request, "index.html",context)

def post_detail(request):
	return HttpResponse('<h1> detallar </h1>')

def post_update(request):
	return HttpResponse('<h1> actualizar </h1>')

def post_delete(request):
	return HttpResponse('<h1> eliminar </h1>')