from django import forms
from .models import BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'text')
        labels = {
                    'title': 'title',
                    'text': 'text'
                  }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'text_f', 'placeholder': 'Write something...'}),
            'title': forms.TextInput(attrs={'class': 'title_f', 'placeholder': 'Heading'}),
        }

