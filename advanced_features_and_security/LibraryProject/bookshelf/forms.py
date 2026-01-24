from django import forms
from .models import Book

# ----------------------------
# ALX expects a form named ExampleForm
# ----------------------------
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    # Optional: simple input cleaning to show security
    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title.strip()

    def clean_author(self):
        return self.cleaned_data.get('author')
