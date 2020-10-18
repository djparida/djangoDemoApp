from django import forms
from .models import Order
from django.contrib.auth.models import User

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_category','payment_method','shipping_cost','unit_price']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
