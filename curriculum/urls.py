from django.urls import path

from . import views


urlpatterns = [
    path('curriculum', views.curriculum, name='curriculum'),
    path('<slug>', views.detail, name = 'detail'),
]
