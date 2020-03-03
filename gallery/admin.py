from django.contrib import admin
from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
admin.site.register(Gallery)