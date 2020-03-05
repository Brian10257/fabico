from django.urls import path

from . import views

urlpatterns = [
    path('gallery_7', views.gallery_7, name='gallery_7'),
]
 