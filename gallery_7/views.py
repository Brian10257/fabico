from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gallery7
from .forms import Gallery7ModelForm


def gallery_7(request):
    gallery7 = Gallery7.objects.order_by('-upload_date')
    paginator = Paginator(gallery7, 54)
    page = request.GET.get('page')
    paged_gallery7 = paginator.get_page(page)
    context = {

        'gallery7': paged_gallery7,

    }

    file_form = Gallery7ModelForm(request.POST, request.FILES)
    files = request.FILES.getlist('file_upload')
    if file_form.is_valid():
        for f in files:
            file_instance = Gallery7(file_upload=f)
            file_instance.save()

    return render(request, 'gallery_7/gallery_7.html', context)
