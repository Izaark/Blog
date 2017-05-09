from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
	next1 = request.GET.get('next')
	title = 'Login'
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		user = form.cleaned_data.get('user')
		password = form.cleaned_data.get('password')
		user = authenticate(username=user, password=password)
		login(request, user)
		if next1:
			return redirect(next1)
		return redirect('/')
	return render(request, 'user/user_login.html', { 'form': form, 'title':title })

def register_view(request):
	title = 'Registrar'
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request,new_user)
		return redirect('/')

	context = {
		'title':title,
		'form':form
		}
	return render(request, 'user/user_login.html', context)

def logout_view(request):
	logout(request)
	return redirect('/')
	return render(request, 'user/user_login.html',{})