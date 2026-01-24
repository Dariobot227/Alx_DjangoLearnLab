from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    # Optional: basic input cleaning for security
    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title.strip()

    def clean_author(self):
        return self.cleaned_data.get('author')
