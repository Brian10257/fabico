from django.db import models
from datetime import datetime
from django.urls import reverse

class Gallery(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField()
    slug = models.SlugField()
    date_added = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title  

    class Meta:
        verbose_name_plural = 'Galleries'

    def get_absolute_url(self):
        return reverse('gallery_detail', kwarg={'slug':self.slug})