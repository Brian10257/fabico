from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('terms_and_usage_conditions/', views.conditions, name='conditions'),
]
