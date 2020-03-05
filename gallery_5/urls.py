from django.urls import path

from . import views

urlpatterns = [
    path('gallery_5', views.gallery_5, name='gallery_5'),
]
