from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gallery3
from .forms import Gallery3ModelForm


def gallery_3(request):
    gallery3 = Gallery3.objects.order_by('-upload_date')
    paginator = Paginator(gallery3, 54)
    page = request.GET.get('page')
    paged_gallery3 = paginator.get_page(page)
    context = {

        'gallery3': paged_gallery3,

    }

    file_form = Gallery3ModelForm(request.POST, request.FILES)
    files = request.FILES.getlist('file_upload')
    if file_form.is_valid():
        for f in files:
            file_instance = Gallery3(file_upload=f)
            file_instance.save()

    return render(request, 'gallery_3/gallery_3.html', context)
