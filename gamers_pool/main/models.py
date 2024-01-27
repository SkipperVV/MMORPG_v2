from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
class Post(models.Model):
    author = models.CharField('Автор', max_length=30, help_text=_("Автор"))
    post_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField('Заголовок', max_length=100, help_text=_("Введите заголовок"))
    text = models.TextField('Содержание', default='Введите техт', help_text=_("Содержание статьи"))
    # post_type = models.CharField(max_length=20, choices=CATEGORY, default='Танки')
    #category = models.ManyToManyField(Category, through='PostCategory')

    def __str__(self):
        return f"{self.title}"
    def get_absolute_url(self):
        return f'/news/{self.id}'
