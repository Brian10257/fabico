from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views import generic
from .models import Gallery

class GalleryList(generic.ListView):
    queryset = Gallery.objects.order_by('-date_added')
    model = Gallery
    template_name = 'pages/photo_galleries.html'
    paginate_by = 6