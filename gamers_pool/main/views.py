import datetime
import os
from urllib import request

from allauth.core.internal.http import redirect
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import get_language as lg
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from .forms import PostForm
from .models import Post
#from .tasks import info_after_new_post

class MainView(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'main/posts.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.now()
        context['posts_quantity'] = len(Post.objects.all())
        return context

class PostView(ListView):
    model = Post
    template_name = 'main/post.html'
    context_object_name = 'post'
    ordering = '-post_time'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        _id = self.kwargs.get('pk')
        context['time_now'] = datetime.datetime.utcnow()
        context['post'] = Post.objects.get(id=_id)
        # context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostCreateView(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    permission_required = ('main.add_post',
                           'main.change_post')
    context_object_name = 'posts_today'
    template_name = 'main/create.html'
    # success_url = '/'   # f'/post<int:{_id}>'# Переделать на стр поста

    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.author = self.request.user
        post.post_time = datetime.date.today()
        form.save()
        # Реализовать рассылку уведомлений после создания новости
        '''info_after_new_post.delay(form.instance.pk)'''
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.utcnow()
        return context

    success_url = reverse_lazy('home')

class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('main.change_post')
    form_class = PostForm
    model = Post
    template_name = 'main/create.html'
    success_url = '/'
    # success_url = f'/post<int:{_id}>
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        _id = self.kwargs.get('pk')
        return Post.objects.get(pk=_id)


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('main.delete_post')
    template_name = 'main/delete.html'
    queryset = Post.objects.all()
    success_url = '/'


def AboutView(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'static/main/txt/', Language(lg()))
    my_file = open(file_path, 'r+', encoding="UTF-8")
    txt = my_file.read()
    my_file.close()

    data = {
        'page': _('О нас'),
        'title': _('Мы очень крутые. Мы самые лучшие!!!!'),
        'text': txt,
    }
    return render(request, 'main/about.html', data)

def CommentViev(request):
    pass
def Language(cur_language):
    if cur_language == 'ru':
        return 'about_ru.txt'
    else:
        return 'about_en.txt'
