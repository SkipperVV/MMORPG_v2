from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('about/', AboutView, name='about'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
]