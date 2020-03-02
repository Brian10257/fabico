from django.db import models
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    subject = models.CharField(max_length = 500, blank = True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Inquiries'