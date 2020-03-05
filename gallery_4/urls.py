from django.urls import path

from . import views

urlpatterns = [
    path('gallery_4', views.gallery_4, name='gallery_4'),
]
