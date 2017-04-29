from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
def post_create(request):
	return HttpResponse('<h1> crear </h1>')

def post_list(request):

	queryset = Post.objects.all()
	context = {
		'queryset':queryset
	}
	return render(request, "index.html",context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
	'title': 'detail',
	'instance' : instance.title,
	}
	return render(request,'index.html',context)

def post_update(request):
	return HttpResponse('<h1> actualizar </h1>')

def post_delete(request):
	return HttpResponse('<h1> eliminar </h1>')