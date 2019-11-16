from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Url

class UrlForm(forms.ModelForm):
	class Meta:
		model = Url
		widgets = {
			'linkTo': forms.TextInput(attrs={'class': 'formLinkTo'}),
			'key': forms.TextInput(attrs={'class': 'formKey'})
		}
		fields=('linkTo', 'key')

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=20, required=False, help_text="Optional.")
	last_name = forms.CharField(max_length=20, required=False, help_text="Optional.")
	email = forms.EmailField(max_length=254, help_text="Required. Enter a valid email address.")

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

