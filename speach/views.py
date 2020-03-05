from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Speach
from django.views.generic import ListView
from django.views import generic


class SpeachList(generic.ListView):
    template_name = 'speach/speach.html'
    queryset = Speach.objects.order_by('date')
    paginate_by = 1
    model = Speach