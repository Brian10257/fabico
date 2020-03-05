from django.urls import path

from . import views


urlpatterns = [
    path('speach', views.SpeachList.as_view(), name='speach'),
]
