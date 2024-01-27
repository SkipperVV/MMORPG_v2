from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'post_time')
    list_filter = ('author', 'post_time')

class PostAdmin(TranslationAdmin):
    model = Post
#class CommentAdmin(TranslationAdmin):
    # model = Comment
admin.site.register(Post, PostsAdmin)
