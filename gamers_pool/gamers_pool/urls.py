from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include


urlpatterns = [
                  path('i18n/', include('django.conf.urls.i18n')),
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('logon/', include('protect.urls')),
                  path('sign/', include('sign.urls')),
                  path('accounts/', include('allauth.urls')),
                  path('comments/', include('django_comments_xtd.urls')),

              ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

