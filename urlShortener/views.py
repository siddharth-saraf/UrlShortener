from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UrlForm, SignUpForm
from .models import Url, LinkClick
import qrcode
from io import BytesIO

def home(request):
	return render(request, 'urlShortener/home.html')

def url_list(request):
	if not request.user.is_authenticated:
		messages.info(request, 'Please login first')
		return HttpResponseRedirect('/accounts/login')
	else:
		return render(request, 'urlShortener/url_list.html', {'urls':Url.objects.filter(owner=request.user).order_by('-dateCreated')})

def redirect(request, key):
	url = get_object_or_404(Url, key=key)
	
	# Check for expiration
	if url.is_expired:
		return render(request, '404.html', {'message': 'This link has expired.'})

	# Log click metrics
	url.clicks += 1
	url.save()
	
	# Record detailed click data
	LinkClick.objects.create(
		url=url,
		referrer=request.META.get('HTTP_REFERER'),
		user_agent=request.META.get('HTTP_USER_AGENT'),
		ip_address=request.META.get('REMOTE_ADDR')
	)
	
	return HttpResponseRedirect(url.linkTo)

def qr_code(request, key):
	url_obj = get_object_or_404(Url, key=key)
	# Construct absolute URL for the shortened link
	full_url = request.build_absolute_uri(f'/r/{url_obj.key}')
	
	qr = qrcode.QRCode(version=1, box_size=10, border=5)
	qr.add_data(full_url)
	qr.make(fit=True)
	
	img = qr.make_image(fill_color="black", back_color="white")
	buffer = BytesIO()
	img.save(buffer, format="PNG")
	return HttpResponse(buffer.getvalue(), content_type="image/png")

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
			messages.success(request, 'Link created successfully!')
			return HttpResponseRedirect('/myUrls/')
	else:
		form = UrlForm()
	return render(request, 'urlShortener/edit_url.html', {'form': form})

def edit_url(request, key):
	if not request.user.is_authenticated:
		messages.info(request, 'Please login first')
		return HttpResponseRedirect('/accounts/login')
	url = get_object_or_404(Url, key=key, owner=request.user)
	if request.method == "POST":
		form = UrlForm(request.POST, instance=url)
		if form.is_valid():
			url = form.save(commit=False)
			url.save()
			messages.success(request, 'Link updated successfully!')
			return HttpResponseRedirect('/myUrls/')
	else:
		form = UrlForm(instance=url)
	return render(request, 'urlShortener/edit_url.html', {'form': form})

def del_url(request, key):
	if not request.user.is_authenticated:
		messages.info(request, 'Please login first')
		return HttpResponseRedirect('/accounts/login')
	url = get_object_or_404(Url, key=key, owner=request.user)
	url.delete()
	messages.success(request, 'Link deleted successfully!')
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