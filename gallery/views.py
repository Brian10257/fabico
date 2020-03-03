from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views import generic
from .models import Gallery

def gallery(request):
    gallery = Gallery.objects.order_by('-date_added')
    return render (request, 'pages/photo_galleries.html', {'gallery':gallery})