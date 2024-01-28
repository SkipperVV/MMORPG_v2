from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('create/', views.PostCreateView.as_view(), name='create'),
]