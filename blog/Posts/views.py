from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


def post_create(request):
	form = PostForm(request.POST or None)
	# if request.method == 'POST':
	# 	print(request.POST)
	# 	print(request.POST.get('title'))
	# 	print(request.POST.get('content'))
	if form.is_valid():
		instance = form.save(commit=False)
		form.cleaned_data.get("title")
		instance.save()
		messages.success(request, 'Se creo correctamente')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	'form': form
	}
	return render(request, 'post_create.html', context)

def post_list(request):

	queryset = Post.objects.all()
	context = {
		'queryset':queryset
	}
	return render(request, "post_list.html",context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
	'title': instance.title,
	'instance' : instance,
	}
	return render(request,'post_detail.html',context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		form.cleaned_data.get("title")
		instance.save()
		messages.success(request, 'Se actualizo !')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	'title' : instance.title,
	'instance': instance,
	'form': form
	}
	return render(request, 'post_create.html', context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, 'Se a eliminado correctamente !')
	return redirect('posts:list')




