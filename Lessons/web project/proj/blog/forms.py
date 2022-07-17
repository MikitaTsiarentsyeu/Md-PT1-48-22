from dataclasses import field
from django import forms
from .models import Post

class AddPost(forms.Form):

    title = forms.CharField(max_length=200, label='Title')
    subtitle = forms.CharField(max_length=500, label='Subtitle')
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'content-textarea'}), label='Content')
    post_type = forms.ChoiceField(choices=Post.POST_TYPES, label='Type')
    image = forms.ImageField(label='Hero image')

    def clean_subtitle(self):

        subtitle_data = self.cleaned_data["subtitle"]
        title_data = self.cleaned_data["title"]

        if subtitle_data == title_data:
            raise forms.ValidationError("the subtitle should differ from the title")

        return subtitle_data

class AddModelFormPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'post_type', 'image')
        label = {'image': "hero image"}

