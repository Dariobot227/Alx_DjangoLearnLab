from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]  # tags included
        widgets = {
            "tags": TagWidget(),  
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
