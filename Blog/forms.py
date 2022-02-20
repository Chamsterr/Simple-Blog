from django import forms
from .models import BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title']
        fields_2 = ['text']
        labels = {
                    'title': 'title',
                    'text': 'text'
                  }