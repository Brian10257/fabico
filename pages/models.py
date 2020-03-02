from django.db import models
from datetime import datetime


class Comment(models.Model):
    image = models.ImageField(upload_to='Post/comments/%Y', blank=True, null=True)
    title = models.CharField(max_length=200)
    comment = models.TextField()
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    comment_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name_plural = 'Home Page'
