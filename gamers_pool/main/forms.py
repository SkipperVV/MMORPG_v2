from django import forms
from django.forms import ModelForm, BooleanField  # true-false поле
from django.utils.translation import gettext as _

from .models import Post


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = _('Выберите категорию')

    check_box = BooleanField(label=_('Сохранить'))

    class Meta:
        model = Post
        fields = ['title', 'category', 'text',  'video', 'audio', 'image', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 100, 'rows': 10, }),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'video': forms.FileInput(attrs={'class': 'form-input'}),
            'audio': forms.FileInput(attrs={'class': 'form-input'}),
            'image': forms.FileInput(attrs={'class': 'form-input'}),
        }
