from django.contrib import admin

from .models import AnualObjective

class AnualObjectiveAdmin(admin.ModelAdmin):
    list_display = ['objective', 'slug', 'created', 'modified']
    search_fields = ['objective']
    list_filter = ['created', 'modified']

admin.site.register(AnualObjective, AnualObjectiveAdmin)
