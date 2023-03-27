from django import forms

from .models import Post


class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['images', 'description']
