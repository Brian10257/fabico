from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from .models import Comment


def index(request):
    if request.method == 'POST':
        image = request.FILES['image']
        name = request.POST['name']
        title = request.POST['title']
        status = request.POST['status']
        comment = request.POST['comment']

        comment = Comment(image=image, name=name, title=title, status=status, comment=comment)
        messages.success(request, 'Your comment has been submitted')
        comment.save()

    comment = Comment.objects.order_by('-comment_date')
    paginator = Paginator(comment, 6)
    page = request.GET.get('page')
    paged_comment = paginator.get_page(page)

    context = {

        'pages': paged_comment,

    }

    return render(request, 'pages/index.html', context)


def conditions(request):
    return render(request, 'pages/conditions.html')