from django.urls import path
from . import views

urlpatterns = [
    path('gallery_1', views.gallery_1, name = 'gallery_1'),
]