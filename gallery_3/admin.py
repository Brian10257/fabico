from django.contrib import admin

from .models import Gallery3


class Gallery3Admin(admin.ModelAdmin):
    list_display = ('name', 'upload_date',)
    list_display_links = ('name', 'upload_date')
    list_filter = ('name', 'upload_date')
    list_per_page = 54

    class Meta():
        model = Gallery3


admin.site.register(Gallery3, Gallery3Admin)
