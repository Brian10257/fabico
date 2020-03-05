from django.urls import path

from . import views

urlpatterns = [
    path('gallery_3', views.gallery_3, name='gallery_3'),
]
