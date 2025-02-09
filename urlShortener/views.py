from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UrlForm, SignUpForm
from .models import Url

def home(request):
	return render(request, 'urlShortener/home.html')

def url_list(request):
	if not request.user.is_authenticated:
		messages.info(request, 'Please login first')
		return HttpResponseRedirect('/accounts/login')
	else:
		return render(request, 'urlShortener/url_list.html', {'urls':Url.objects.filter(owner=request.user).order_by('dateCreated')})

def redirect(request, key):
	try:
		url = get_object_or_404(Url, key=key)
		return HttpResponseRedirect(url.linkTo)
	except:
		return HttpResponseRedirect('/')

def new_url(request):
	if not request.user.is_authenticated:
		messages.info(request, 'Please login first')
		return HttpResponseRedirect('/accounts/login')
	if request.method == "POST":
		form = UrlForm(request.POST)
		if form.is_valid():
			url = form.save(commit=False)
			url.owner = request.user
			url.save()
			return HttpResponseRedirect('/myUrls/')
	else:
		form = UrlForm
	return render(request, 'urlShortener/edit_url.html', {'form': form})

def edit_url(request, key):
	if not request.user.is_authenticated:
		messages.info(request, 'Please login first')
		return HttpResponseRedirect('/accounts/login')
	url = get_object_or_404(Url, key=key)
	if request.method == "POST":
		form = UrlForm(request.POST, instance=url)
		if form.is_valid():
			url = form.save(commit=False)
			url.owner = request.user
			url.save()
			return HttpResponseRedirect('/myUrls/')
	else:
		form = UrlForm(instance=url)
	return render(request, 'urlShortener/edit_url.html', {'form': form})

def del_url(request, key):
	if not request.user.is_authenticated:
		messages.success(request, 'Please login first')
		return HttpResponseRedirect('/accounts/login')
	url = get_object_or_404(Url, key=key)
	url.delete()
	return HttpResponseRedirect('/myUrls/')

def edit_account(request):
	if not request.user.is_authenticated:
		messages.success(request, 'Please login first')
		return HttpResponseRedirect('/accounts/login')
	user = request.user
	if request.method == "POST":
		form = SignUpForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form  = SignUpForm(instance=user)
	return render(request, 'registration/signup.html', {'form': form})

def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username= form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username= username, password= raw_password)
			login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = SignUpForm
	return render(request, 'registration/signup.html', {'form': form})