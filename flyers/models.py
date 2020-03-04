from django.db import models
from datetime import datetime


class Flyer(models.Model):
    doc = models.FileField(upload_to='Prospectus/%Y', blank=True, null=True)
    name = models.CharField(max_length=5000, blank=True)
    description = models.TextField(blank=True)
    date_published = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Flyers'