from django.shortcuts import render
import datetime
from .forms import PostForm
from .models import Post
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, View


def MainView(request):
    data = {
        'page': 'Главная страница',
        'title': 'Заглавие главной страницы',
        'text': 'Наполнение главной страницы главной страницы главной страницыглавной страницыглавной страницыглавной страницы',
    }
    return render(request, 'main/home.html', data)


def AboutView(request):
    data = {
        'page': 'О нас',
        'title': 'Заглавие рассказа о себе',
        'text': 'Рассказ о нас, любимых. Рассказ о нас, любимых. Рассказ о нас, любимых. Рассказ о нас, любимых. Рассказ о нас, любимых. Рассказ о нас, любимых. Рассказ о нас, любимых. Рассказ о нас, любимых.Рассказ о нас, любимых. Рассказ о нас, любимых. Рассказ о нас, любимых. Рассказ о нас, любимых.',
    }
    return render(request, 'main/home.html', data)
    # return render(request, 'main/about.html')


class PostCreateView(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'main/create.html'
    permission_required = ('Models.add_post',
                           'Models.change_post')
    context_object_name = 'posts_today'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        #author =self.request.user.username
        # form.instance.author = self.request.user#.author
        today = datetime.date.today()
        post.save()
        #Реализовать рассылку уведомлений подписчикам после создания новости
        #info_after_new_post.delay(form.instance.pk)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.datetime.utcnow()
        # context['how_many'] = Post.objects.filter()
        return context