from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gallery6
from .forms import Gallery6ModelForm


def gallery_6(request):
    gallery6 = Gallery6.objects.order_by('-upload_date')
    paginator = Paginator(gallery6, 54)
    page = request.GET.get('page')
    paged_gallery6 = paginator.get_page(page)
    context = {

        'gallery6': paged_gallery6,

    }

    file_form = Gallery6ModelForm(request.POST, request.FILES)
    files = request.FILES.getlist('file_upload')
    if file_form.is_valid():
        for f in files:
            file_instance = Gallery6(file_upload=f)
            file_instance.save()

    return render(request, 'gallery_6/gallery_6.html', context)
