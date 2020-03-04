from django.shortcuts import render
from django.views import generic
from .models import Flyer
from django.views.generic import ListView

class FlyerList(generic.ListView):
    queryset = Flyer.objects.order_by('-date_published')
    model = Flyer
    paginate_by = 1
    template_name = 'pages/flyer.html'