from django.contrib import admin
from .models import Career

class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'place_of_birth', 'application_date')
    list_display_links = ('name', 'email')
    list_filter = ('name', 'place_of_birth', 'application_date')
    search_fields = ('name', 'place_of_birth', 'phone_number', 'neighbour_hood')
admin.site.register(Career, CareerAdmin)