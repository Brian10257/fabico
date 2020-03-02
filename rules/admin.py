from django.contrib import admin
from .models import Rules

class RulesAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
    list_display_links = ('title', 'name')
    list_filter = ('title', 'name')
    search_fields = ('title', 'name')
admin.site.register(Rules, RulesAdmin)