from django.db import models
from datetime import datetime


class About(models.Model):
    image = models.ImageField(upload_to='about/administration/%Y', blank=True)
    name = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    speach = models.TextField(blank=True, null=True)
    possision = models.CharField(max_length=100, blank=True)
    history = models.TextField(blank=True)
    date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'About'
