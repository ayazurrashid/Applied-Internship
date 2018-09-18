from django.core.exceptions import ValidationError
from django import forms

class comp_form(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	title = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	address = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	city = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	pincode = forms.CharField(widget=forms.NumberInput(attrs={
		'class':'form-control'
		}))
	discription = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	email = forms.EmailField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	url = forms.URLField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control'
		}))
class edit_form(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	title = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	address = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	city = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	pincode = forms.CharField(widget=forms.NumberInput(attrs={
		'class':'form-control'
		}))
	discription = forms.CharField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	email = forms.EmailField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	url = forms.URLField(widget=forms.TextInput(attrs={
		'class':'form-control'
		}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control'
		}))
