from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views.generic import ListView, DetailView
from django.views import generic
from django.contrib import messages
from .forms import CommentForm

class BlogList(generic.ListView):
    queryset = Blog.objects.order_by('-date_published')
    template_name = 'blog/blog.html'
    paginate_by = 6
    model = Blog


def blog_detail(request, slug):
    template_name = 'blog/blog_detail.html'
    post = get_object_or_404(Blog, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            messages.success(request, ': Comment Posted Successfuly')
    else:
        comment_form = CommentForm()

    context = {'post': post,
               'comments': comments,
               'new_comment': new_comment,
               'comment_form': comment_form}
    
    return render(request, template_name, context)
