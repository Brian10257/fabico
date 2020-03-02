from django.db import models
from datetime import datetime


class Rules(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    name = models.CharField(max_length=10000, blank=True)
    description = models.TextField(blank=True)
    date_issued = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Rules and Regulations'
