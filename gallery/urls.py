from django.urls import path

from . import views

urlpatterns = [
    path('photo_galleries/app', views.gallery, name='gallery'),
]
