from django import forms
from .models import Item, Contact


class AddContact(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ['create_date', 'last_modified_date']


class AddItem(forms.ModelForm):

    class Meta:
        model = Item
        exclude = [
            'is_active', 'create_date', 'last_modified_date', 'who_found',
            'who_lost'
        ]
