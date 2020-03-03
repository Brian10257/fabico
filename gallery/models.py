from django.db import models
from datetime import datetime

class Gallery(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add = True, blank = True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Galleries'