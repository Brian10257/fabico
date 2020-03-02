from django.contrib import admin
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'date_published')
    list_display_links = ('title', 'name')
    list_filter = ('title', 'name', 'date_published')
    search_fields = ('title', 'name')
    prepopulated_fields = {'slug':('title', 'name')}
admin.site.register(Blog, BlogAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'comment_date', 'active')
    list_display_links = ['name', 'post']
    list_filter = ('active', 'comment_date')
    list_per_page = 90
    list_editable = ('active',)
    search_fields = ('name', 'email', 'body', 'website')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
