from django.urls import path, include
from . import views
from .views import PostUpdateView, PostDeleteView, PostView

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('about/', views.AboutView, name='about'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('post/<int:pk>', PostView.as_view(), name='posts'),
]