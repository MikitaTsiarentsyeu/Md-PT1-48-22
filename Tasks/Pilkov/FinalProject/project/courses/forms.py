from django import forms
from .models import Course

class AddCourseModelForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('name', 'description', 'image', )
        label = {'image': "course image"}