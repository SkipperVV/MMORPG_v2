from django.forms import ModelForm, TextInput

from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        author = 'author'#how to get a user?
        fields = [author, 'title', 'text', ]
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите заголовок",

            }),
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "А сюда - содержание",

            })


        }
