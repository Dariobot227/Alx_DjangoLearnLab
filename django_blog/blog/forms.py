from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma separated tags")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()

        tag_names = self.cleaned_data["tags"].split(",")

        instance.tags.clear()

        for tag_name in tag_names:
            tag_name = tag_name.strip()
            if tag_name:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)

        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
