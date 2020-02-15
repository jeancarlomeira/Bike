from django.contrib import admin

from .models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['distance', 'date', 'slug', 'created', 'modified']
    search_fields = ['distance', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('distance', 'date')}

admin.site.register(Activity, ActivityAdmin)
