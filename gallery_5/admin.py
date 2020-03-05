from django.contrib import admin

from .models import Gallery5


class Gallery5Admin(admin.ModelAdmin):
    list_display = ('name', 'upload_date',)
    list_display_links = ('name', 'upload_date')
    list_filter = ('name', 'upload_date')
    list_per_page = 54

    class Meta():
        model = Gallery5


admin.site.register(Gallery5, Gallery5Admin)
