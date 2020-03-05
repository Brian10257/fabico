from django.contrib import admin

from .models import Gallery2


class Gallery2Admin(admin.ModelAdmin):
    list_display = ('name', 'upload_date',)
    list_display_links = ('name', 'upload_date')
    list_filter = ('name', 'upload_date')
    list_per_page = 54

    class Meta():
        model = Gallery2


admin.site.register(Gallery2, Gallery2Admin)
