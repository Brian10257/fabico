from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Curriculum


def curriculum(request):
    curriculum = Curriculum.objects.order_by('-edit_date')
    paginator = Paginator(curriculum, 6)
    page = request.GET.get('page')
    paged_curriculum = paginator.get_page(page)
    context = {

        'curriculum': paged_curriculum,

    }
    return render(request, 'curriculum/curriculum.html', context)
