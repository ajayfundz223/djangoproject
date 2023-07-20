from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter description', 'class': 'form-control w-50'}))
    price = forms.FloatField()
    image = forms.ImageField()
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')