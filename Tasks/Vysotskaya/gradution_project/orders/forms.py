from dataclasses import fields
from django import forms
from .models import Order
from blog.models import Services

class OrderForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Services.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Order
        fields = ['service', 'name', 'phone']


  