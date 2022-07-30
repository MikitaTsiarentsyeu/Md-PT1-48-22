
from django.forms import TextInput,Textarea
from django import forms
from .models import registration

class AddModelFormRecord(forms.ModelForm):

    class Meta:
        model= registration
        fields = ('name','phone','auto','year','service','comment' )
        widgets= {'name':TextInput(attrs={'class':'form-control',
            'placeholder':'Введите ваше имя', 
        }),
        'phone':TextInput(attrs={"class":'form-control',
            'placeholder':'Номер в формате (хх)ххххххх' 
        }),
        'auto':TextInput(attrs={
            'class':'form-control',
            'placeholder':'Введите марку и модель' 
        }),
        'year':TextInput(attrs={"class":'form-control',
            'placeholder':'Введите год вашего авто' 
        }),
        'service':TextInput(attrs={
            'class':'form-control',
            'placeholder':'введите требуемые услуги' 
        }),
        'comment':Textarea(attrs={
            'class':'form-control',
            'placeholder':'Опишите вашу проблему',
            
        }),
        }
        


