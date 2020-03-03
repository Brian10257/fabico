from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Curriculum


def curriculum(request):
    curriculum = Curriculum.objects.order_by('-date_published')
    paginator = Paginator(curriculum, 6)
    page = request.GET.get('page')
    paged_curriculum = paginator.get_page(page)
    context = {

        'curriculum': paged_curriculum,

    }
    return render(request, 'curriculum/curriculum.html', context)

def detail(request, slug):
    detail = get_object_or_404(Curriculum, slug=slug)

    context = {
        'detail': detail
        }

    return render(request, 'curriculum/curriculum_detail.html', context)
