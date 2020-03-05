from django.contrib import admin

from .models import Gallery6


class Gallery6Admin(admin.ModelAdmin):
    list_display = ('name', 'upload_date',)
    list_display_links = ('name', 'upload_date')
    list_filter = ('name', 'upload_date')
    list_per_page = 54

    class Meta():
        model = Gallery6


admin.site.register(Gallery6, Gallery6Admin)
 