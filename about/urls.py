from django.urls import path
from . import views

urlpatterns = [
    path('about_fabico/', views.about, name = 'about')
]