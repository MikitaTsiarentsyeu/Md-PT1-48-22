from dataclasses import field
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'article',
            'brend',
            'cross', 
            'quantity', 
            'cost',
            'parsing_date',
        )
        widgets = {
            'article': forms.TextInput,
            'brend': forms.TextInput,
            'cross': forms.TextInput,
            'quantity': forms.TextInput,
        }


class NameForm(forms.Form):
    number = forms.CharField(label='number', max_length=100)
    print(number)