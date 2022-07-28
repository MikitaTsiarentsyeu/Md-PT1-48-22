from django import forms
from .models import Theme, Information

class AddTheme(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ('title',)
        label = {'title':"На какую тему ты хочешь пообщаться?"}

class AddInformation(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('content', 'images')
        label = {'content':"Ввод", 'images':"Картинка"}