from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Url

class UrlForm(forms.ModelForm):
	class Meta:
		model = Url
		widgets = {
			'linkTo': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com/very-long-url'}),
			'key': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'custom-slug'}),
			'expires_at': forms.DateTimeInput(
				attrs={'class': 'form-control', 'type': 'datetime-local'},
				format='%Y-%m-%dT%H:%M'
			),
		}
		fields=('linkTo', 'key', 'expires_at')
		labels = {
			'linkTo': 'Destination URL',
			'key': 'Custom Slug (Key)',
			'expires_at': 'Expiration Date (Optional)',
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# Ensure the datetime-local widget gets the correct format for initial data
		if self.instance and self.instance.expires_at:
			self.initial['expires_at'] = self.instance.expires_at.strftime('%Y-%m-%dT%H:%M')

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=20, required=False, help_text="Optional.")
	last_name = forms.CharField(max_length=20, required=False, help_text="Optional.")
	email = forms.EmailField(max_length=254, help_text="Required. Enter a valid email address.")

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

