from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


# class PostsAdmin(admin.ModelAdmin):
#     list_display = ('author', 'title', 'post_time')
#     list_filter = ('author', 'post_time')

class PostAdmin(TranslationAdmin):
    model = Post
#class CommentAdmin(TranslationAdmin):
    # model = Comment
#admin.site.register(Post, PostsAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('author',) # скрыть author поле, чтобы оно не отображалось в форме изменений

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

