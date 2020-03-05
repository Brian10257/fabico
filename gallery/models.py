from django.db import models
from datetime import datetime
from django.urls import reverse

class Gallery(models.Model):
    title = models.CharField(max_length=300, verbose_name='Album Name')
    image = models.ImageField()
    url_album = models.CharField(max_length=300, blank = True)
    uploaded_on = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Date Uploaded')
    
    class Meta:
        verbose_name_plural = "Galleries"

    def get_absolute_url(self):
        return reverse('gallery', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title