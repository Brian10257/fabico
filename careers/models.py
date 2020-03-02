from django.db import models
from datetime import datetime


class Career(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    place_of_birth = models.CharField(max_length=200)
    current_city = models.CharField(max_length=200)
    neighbour_hood = models.CharField(max_length=200)
    current_employment = models.CharField(max_length=1000)
    subject = models.CharField(max_length = 500, blank = True)
    message = models.TextField()
    file_upload = models.FileField(upload_to='Applications/Files/%Y')
    application_date = models.DateTimeField(auto_now_add=True, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Job Applications Recieved'