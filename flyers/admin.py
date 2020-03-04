from django.contrib import admin
from .models import Flyer

class FlyerAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_published']
    list_display_links = ['name', 'date_published']
    search_fields = ['name']
    list_filter = ['name', 'date_published']

admin.site.register(Flyer, FlyerAdmin)