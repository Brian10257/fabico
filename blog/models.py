from django.db import models
from datetime import datetime
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length = 200, blank = True)
    name = models.CharField(max_length=200, blank = True)
    image = models.ImageField()
    description = models.TextField()
    slug = models.SlugField()
    date_published = models.DateTimeField(auto_now_add=True, blank = True)
    facebook = models.URLField(max_length = 20000, blank = True)
    twiter = models.URLField(max_length=20000, blank=True)
    instagram = models.URLField(max_length=20000, blank=True)
    google_plus = models.URLField(max_length=20000, blank=True)
    linkedin = models.URLField(max_length=20000, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='Blog Posts'

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug':self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50000)
    email = models.EmailField(max_length=5000, blank=True)
    website = models.CharField(max_length=5000, blank=True)
    body = models.TextField()
    active = models.BooleanField(default=True)
    comment_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['comment_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)