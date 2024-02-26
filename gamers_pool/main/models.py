from PIL import Image, ImageOps
from django.conf import settings
from django.contrib.auth.models import User,Group
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator

CATEGORY = [('Танки', 'Танки'), ('Хилы', 'Хилы',), ('ДД', 'ДД'), ('Торговцы', 'Торговцы'),
            ('Гилдмастеры', 'Гилдмастеры'), ('Квестгиверы', 'Квестгиверы'), ('Кузнецы', 'Кузнецы'),
            ('Кожевники', 'Кожевники'), ('Зельевары', 'Зельевары'), ('Мастера заклинаний', 'Мастера заклинаний')]



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text=_("Автор"))
    nickname = models.CharField(max_length=100, help_text=_("Никнейм"))

    def add_to_group(self):
        user=self.user
        user.groups.add(Group.objects.get(name='gamer'))

    def __str__(self):
        return self.user.username


class Post(models.Model):
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'author_{0}/{1}'.format(instance.author.id, filename)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, help_text=_("Автор"))
    '''https://ru.stackoverflow.com/questions/972537/%D0%9A%D0%B0%D0%BA-%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8-%D0%B2%D0%BD%D0%BE%D1%81%D0%B8%D1%82%D1%8C-%D0%B8%D0%BC%D1%8F-%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D0%B8%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F-%D0%B2-%D0%BF%D0%BE%D0%BB%D0%B5-%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8'''
    post_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(_('Заголовок'), max_length=50, help_text=_("Введите заголовок"))
    text = models.TextField(_('Содержание'), help_text=_("Содержание статьи"))
    category = models.CharField(_('Категория'), max_length=20, choices=CATEGORY, help_text=_('Введите категорию'))
    video = models.FileField('video', upload_to=user_directory_path, blank=True, null=True)
    audio = models.FileField('audio', upload_to=user_directory_path, blank=True, null=True)
    image = models.ImageField('image', upload_to=user_directory_path, blank=True, )
    enable_comments = models.BooleanField(default=True,)



    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     image = Image.open(self.image.path)
    #
    #     if image.height > 500 or image.width > 500:
    #         if image.height > image.width:
    #             factor = 500 / image.height
    #             nH = 500
    #             nW = image.width * factor
    #             output_size = (nH, nW)
    #         if image.width > image.height:
    #             factor = 500 / image.width
    #             nW = 500
    #             nH = image.height * factor
    #             output_size = (nH, nW)
    #         else:
    #             output_size = (500, 500)
    #         image = ImageOps.exif_transpose(image)
    #
    #         image.thumbnail(output_size)
    #         image.save(self.image.path)

    def __str__(self):
        return f"{self.title[:20]}"

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

class PostCommentModerator(CommentModerator):
    email_notification = True
    auto_moderate_field = 'post_time'
    moderate_after = 365

moderator.register(Post, PostCommentModerator)