from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['title', 'name', 'status']
    list_display_links = ['title', 'name']
    list_filter = ['title', 'name']
    list_per_page = 50
admin.site.register(Comment, CommentAdmin)