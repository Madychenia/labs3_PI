from django import forms
from .models import Item
from django.contrib.auth.models import User

class ItemForm(forms.ModelForm):

	class Meta:
		model = Item
		fields = ('title', 'price',)

class LoginForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('email', 'password',)