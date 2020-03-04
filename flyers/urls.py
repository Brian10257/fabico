from django.urls import path
from . import views

urlpatterns = [
    path('prospectus/', views.FlyerList.as_view(), name = 'flyer'),
]