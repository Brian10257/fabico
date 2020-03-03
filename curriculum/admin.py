from django.contrib import admin

from .models import Curriculum


class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('subject', 'edit_date',)
    list_display_links = ('subject', 'edit_date')
    list_filter = ('subject', 'edit_date')
    prepopulated_fields = {'slug':('subject',)}
    list_per_page = 50

    class Meta():
        model = Curriculum


admin.site.register(Curriculum, CurriculumAdmin)
