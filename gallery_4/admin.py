from django.contrib import admin

from .models import Gallery4


class Gallery4Admin(admin.ModelAdmin):
    list_display = ('name', 'upload_date',)
    list_display_links = ('name', 'upload_date')
    list_filter = ('name', 'upload_date')
    list_per_page = 54

    class Meta():
        model = Gallery4


admin.site.register(Gallery4, Gallery4Admin)
