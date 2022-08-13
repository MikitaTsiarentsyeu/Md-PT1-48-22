from email.mime import image
from django import forms
from .models import Post,Services
from django.http import HttpResponseRedirect 
from django.urls import reverse

class AddPost (forms.Form):

    title = forms.CharField(widget=forms.Textarea(attrs={'class':'content-textarea'}), label="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'content-textarea'}), label="Text")
    image = forms.ImageField(label="Photo")





        