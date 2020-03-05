from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gallery2
from .forms import Gallery2ModelForm


def gallery_2(request):
    gallery2 = Gallery2.objects.order_by('-upload_date')
    paginator = Paginator(gallery2, 54)
    page = request.GET.get('page')
    paged_gallery2 = paginator.get_page(page)
    context = {

        'gallery2': paged_gallery2,

    }

    file_form = Gallery2ModelForm(request.POST, request.FILES)
    files = request.FILES.getlist('file_upload')
    if file_form.is_valid():
        for f in files:
            file_instance = Gallery2(file_upload=f)
            file_instance.save()

    return render(request, 'gallery_2/gallery_2.html', context)
