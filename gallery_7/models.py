from django.db import models

from datetime import datetime


class Gallery7(models.Model):
    name = models.CharField(max_length=200, blank=True)
    file_upload = models.FileField(upload_to='Pictures/Gallery7/%Y')
    description = models.TextField(blank=True)
    upload_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Gallery 7'
