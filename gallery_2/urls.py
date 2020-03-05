from django.urls import path

from . import views

urlpatterns = [
    path('gallery_2', views.gallery_2, name='gallery_2'),
]
