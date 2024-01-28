from django.forms import ModelForm, BooleanField  # true-false поле
from .models import Post


class PostForm(ModelForm):
    check_box = BooleanField(label='Сохранить')
    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'check_box']
        exclude = ["post_time", "author"]
