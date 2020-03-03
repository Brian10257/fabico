from django.contrib import admin

from .models import Curriculum


class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('subject', 'crew', 'date_published',)
    list_display_links = ('subject', 'crew')
    list_filter = ('subject', 'crew', 'date_published')
    prepopulated_fields = {'slug': ('subject',)}
    list_per_page = 50

    class Meta():
        model = Curriculum


admin.site.register(Curriculum, CurriculumAdmin)
