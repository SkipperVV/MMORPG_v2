from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

CATEGORY = (('Танки', 'Танки'), ('Хилы', 'Хилы',), ('ДД', 'ДД'), ('Торговцы', 'Торговцы'),
            ('Гилдмастеры', 'Гилдмастеры'), ('Квестгиверы', 'Квестгиверы'), ('Кузнецы', 'Кузнецы,'),
            ('Кожевники', 'Кожевники'), ('Зельевары', 'Зельевары'), ('Мастера заклинаний', 'Мастера заклинаний'))


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, help_text=_("Автор"))
    # author = models.CharField('Автор', max_length=30, help_text=_("Автор"))
    '''https://ru.stackoverflow.com/questions/972537/%D0%9A%D0%B0%D0%BA-%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8-%D0%B2%D0%BD%D0%BE%D1%81%D0%B8%D1%82%D1%8C-%D0%B8%D0%BC%D1%8F-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F-%D0%B2-%D0%BF%D0%BE%D0%BB%D0%B5-%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8'''
    post_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(_('Заголовок'), max_length=100, help_text=_("Введите заголовок"))
    text = models.TextField(_('Содержание'), help_text=_("Содержание статьи"))
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    category = models.CharField(_('Категория'), max_length=20, choices=CATEGORY, help_text=_('Введите категорию'))

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return f'/news/{self.id}'


class Comment(models.Model):
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Коментании от автора {self.user}: {self.text}"
