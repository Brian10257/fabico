from django.contrib import admin
from .models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'possision']
    list_display_links = ['name', 'title']
    list_filter = ['name', 'title']
    search_fields = ['name', 'title', 'possision']
admin.site.register(About, AboutAdmin)
