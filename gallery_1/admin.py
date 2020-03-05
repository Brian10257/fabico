from django.contrib import admin

from .models import Gallery1


class Gallery1Admin(admin.ModelAdmin):
    list_display = ('name', 'upload_date',)
    list_display_links = ('name', 'upload_date')
    list_filter = ('name', 'upload_date')
    list_per_page = 54

    class Meta():
        model = Gallery1


admin.site.register(Gallery1, Gallery1Admin)
