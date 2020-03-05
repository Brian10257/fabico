from django.contrib import admin

from .models import Gallery7


class Gallery7Admin(admin.ModelAdmin):
    list_display = ('name', 'upload_date',)
    list_display_links = ('name', 'upload_date')
    list_filter = ('name', 'upload_date')
    list_per_page = 54

    class Meta():
        model = Gallery7


admin.site.register(Gallery7, Gallery7Admin)
 