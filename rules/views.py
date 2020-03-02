from django.shortcuts import render
from . models import Rules
from django.views.generic import ListView
from django.views import generic

class RulesList(generic.ListView):
    queryset = Rules.objects.all()
    model = Rules
    template_name = 'pages/rules.html'
    paginate_by = 1