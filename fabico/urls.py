from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', include('about.urls')),
    path('', include('pages.urls')),
    path('blogs/', include('blog.urls')),
    path('careers/', include('careers.urls')),
    path('gallery/', include('gallery.urls')),
    path('inquiry/', include('contact.urls')),
    path('School_rules/', include('rules.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
