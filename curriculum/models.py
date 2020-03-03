from django.db import models
from datetime import datetime
from django.urls import reverse

POSITION=(
    ('400ms', '400ms'),
    ('500ms', '500ms'),
    ('600ms', '600ms'),
    ('700ms', '700ms'),

)

class Curriculum(models.Model):
    subject = models.CharField(max_length=200)
    crew = models.CharField(max_length=5000, blank=True, verbose_name='Available Teachers')
    follow_up_by = models.CharField(max_length=5000, blank=True)
    period_tought = models.CharField(max_length=5000, blank=True)
    description = models.TextField()
    possision = models.CharField(max_length=10, blank=True, choices=POSITION, default='400ms')
    edit_date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = 'Curriculum'

    def get_absolute_url(self):
        return reverse('subject', kwargs={'slug': self.slug})
