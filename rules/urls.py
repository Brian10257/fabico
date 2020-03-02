from django.urls import path
from . import views

urlpatterns = [
    path('regulations/', views.RulesList.as_view(), name = 'rules')
]