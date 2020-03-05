from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gallery4
from.forms import Gallery4ModelForm


def gallery_4(request):
    gallery4 = Gallery4.objects.order_by('-upload_date')
    paginator = Paginator(gallery4, 54)
    page = request.GET.get('page')
    paged_gallery4 = paginator.get_page(page)
    context = {

        'gallery4': paged_gallery4,

    }

    file_form = Gallery4ModelForm(request.POST, request.FILES)
    files = request.FILES.getlist('file_upload')
    if file_form.is_valid():
        for f in files:
            file_instance = Gallery4(file_upload=f)
            file_instance.save()

    return render(request, 'gallery_4/gallery_4.html', context)
