from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product
from django.contrib.auth import password_validation
from ckeditor.widgets import CKEditorWidget
class RegistrationForm(UserCreationForm):
    firstname = forms.CharField(required=True, label="First Name", widget=forms.TextInput(attrs={'class': "mb-3 w-full"}))
    lastname = forms.CharField(required=True, label="Last Name",widget=forms.TextInput(attrs={'class': "mb-3 w-full"}))
    email = forms.CharField(required=True, label="email",widget=forms.EmailInput(attrs={'class': "mb-3 w-full"}))
    # password1 = forms.CharField(required=True, label="password", validators=[password_validation.CommonPasswordValidator], widget=forms.PasswordInput(attrs={'class': "mb-3 w-full"}))
    # password2 = forms.CharField(required=True, label="password",widget=forms.PasswordInput(attrs={'class': "mb-3 w-full"}))

     
    class Meta:
        model = User
        fields = ["firstname", "lastname", "username", "email", "password1", "password2"] 
        
class ProductForm(forms.Form):
    name = forms.CharField(label="name")
    price = forms.IntegerField(label="price")
    quantity_available = forms.IntegerField(label="Quantity Available")
    description = forms.CharField(label="description", widget=CKEditorWidget())
    image = forms.ImageField(label="Product Image")
    
    class meta:
        model = Product
        fields = ['name', 'price', 'quantity_available', 'image', 'description']