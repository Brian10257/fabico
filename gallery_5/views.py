from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gallery5
from .forms import Gallery5ModelForm


def gallery_5(request):
    gallery5 = Gallery5.objects.order_by('-upload_date')
    paginator = Paginator(gallery5, 54)
    page = request.GET.get('page')
    paged_gallery5 = paginator.get_page(page)
    context = {

        'gallery5': paged_gallery5,

    }

    file_form = Gallery5ModelForm(request.POST, request.FILES)
    files = request.FILES.getlist('file_upload')
    if file_form.is_valid():
        for f in files:
            file_instance = Gallery5(file_upload=f)
            file_instance.save()

    return render(request, 'gallery_5/gallery_5.html', context)
