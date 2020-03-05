from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gallery1
from .forms import Gallery1ModelForm

 
def gallery_1(request):
    gallery1 = Gallery1.objects.order_by('-upload_date')
    paginator = Paginator(gallery1, 54)
    page = request.GET.get('page')
    paged_gallery1 = paginator.get_page(page)
    context = {

        'gallery1': paged_gallery1,

    }

    file_form = Gallery1ModelForm(request.POST, request.FILES)
    files = request.FILES.getlist('file_upload')
    if file_form.is_valid():
        for f in files:
            file_instance = Gallery1(file_upload=f)
            file_instance.save()

    return render(request, 'gallery_1/gallery_1.html', context)
