from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Gallery)

@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'category',)
    prepopulated_fields = {'slug':('link',)}