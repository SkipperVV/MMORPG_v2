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

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
