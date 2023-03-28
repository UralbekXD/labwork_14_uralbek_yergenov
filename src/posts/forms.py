from django import forms

from .models import Post, Comment


class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['images', 'description']


# class CommentAddForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text']
