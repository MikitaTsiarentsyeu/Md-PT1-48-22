from django import forms

from .models import Course

class AddCourseModelForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('name', 'description', 'image', )
        label = {'image': "course image"}

class AddLectionForm(forms.Form):
    title = forms.CharField(max_length=80, label='Title')
    text = forms.CharField(max_length=1000, widget=forms.Textarea(), required=False, label='Lection text')
    video = forms.FileField(widget=forms.FileInput(attrs={'accept': '.mp4'}), label='Video')
