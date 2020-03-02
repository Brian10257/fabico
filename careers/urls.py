from django.urls import path
from . import views

urlpatterns = [
    path('application/', views.career, name = 'career'),
]