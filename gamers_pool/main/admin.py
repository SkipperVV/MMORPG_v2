from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post, Author#,Comment
# admin.site.register(Comment)


# class PostAdmin(TranslationAdmin):
#     model = Post


# class CommentAdmin(TranslationAdmin):
#     model = Comment

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ('user', 'nickname',)
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('pk','author', 'title', 'post_time')
    list_filter = ('author', 'post_time')

    # exclude = ('author',) # скрыть author поле, чтобы оно не отображалось в форме изменений



    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)



