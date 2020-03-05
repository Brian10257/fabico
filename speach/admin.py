from django.contrib import admin

from .models import Speach 


class SpeachAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
    list_display_links = ('title', 'name')
    list_filter = ('title', 'name')
    search_fields = ('name', 'title')
    list_per_page = 50

    class Meta():
        model = Speach


admin.site.register(Speach, SpeachAdmin)
