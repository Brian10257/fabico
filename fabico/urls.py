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
    path('hand_bills', include('flyers.urls')),
    path('programme/', include('curriculum.urls')),
    path('gallery/', include('gallery.urls')),
    path('staff/', include('gallery_1.urls')),
    path('extra_curricular/activities/', include('gallery_2.urls')),
    path('sports/', include('gallery_3.urls')),
    path('prefects/', include('gallery_4.urls')),
    path('administration/', include('gallery_5.urls')),
    path('staff/', include('gallery_6.urls')),
    path('staff/', include('gallery_7.urls')),
    path('inquiry/', include('contact.urls')),
    path('welcome/', include('speach.urls')),
    path('School_rules/', include('rules.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
