from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote_plus
from django.utils import timezone
from django.db.models import Q
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType

def post_create(request):
	if not request.user.is_authenticated():
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		form.cleaned_data.get("title")
		instance.user = request.user
		instance.save()
		messages.success(request, 'Se creo correctamente')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	'form': form
	}
	return render(request, 'post_create.html', context)

def post_list(request):
	today = timezone.now()
	queryset_list = Post.objects.active()	#filter(draft=False).filter(publish__lte=timezone.now())	#.order_by('-timestamp')
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()
	query = request.GET.get('q')	#busqueda
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(user__first_name__icontains=query)).distinct()

	paginator = Paginator(queryset_list, 5)
	page_request_var = "list"
	page = request.GET.get(page_request_var)
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
	context = {
	'object_list':queryset,
	'page_request_var':page_request_var,
	'today':today
	}

	return render(request, "post_list.html",context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.title)
	content_type = ContentType.objects.get_for_model(Post)
	object_id = instance.id
	comments = Comment.objects.filter(content_type=content_type, object_id=object_id)
	context = {
	'title': instance.title,
	'instance' : instance,
	'share_string' : share_string,
	'comments' : comments
	}
	return render(request,'post_detail.html',context)

def post_update(request, slug=None):
	if not request.user.is_authenticated():
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance = instance)
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
	return render(request, 'post_update.html', context)

def post_delete(request, slug=None):
	if not request.user.is_authenticated():
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, 'Se a eliminado correctamente !')
	return redirect('posts:list')




