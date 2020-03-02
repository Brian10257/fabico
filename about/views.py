from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import About


def about(request):
    about = About.objects.all()
    paginator = Paginator(about, 4)
    page = request.GET.get('page')
    paged_about = paginator.get_page(page)

    context = {

        'about': paged_about,

    }
    
    return render(request, 'pages/about.html', context)
