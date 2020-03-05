from django.db import models
from datetime import datetime


class Speach(models.Model):
    image = models.FileField(upload_to='Speach/%Y', blank=True)
    title = models.CharField(max_length=5000, blank=True)
    name = models.CharField(max_length=5000, blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str_(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Speaches'
