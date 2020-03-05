from django.urls import path

from . import views

urlpatterns = [
    path('photo_galleries/app', views.GalleryList.as_view(), name='gallery'),
]
