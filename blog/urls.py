from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogList.as_view(), name = 'blog_post'),
    path('<slug>/', views.blog_detail, name = 'blog_detail'), 
]