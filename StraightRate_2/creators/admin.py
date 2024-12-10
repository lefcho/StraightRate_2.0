from django.contrib import admin
from .models import Director, Developer


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('id', 'developer_name',)
    list_display_links = ('developer_name',)
    search_fields = ('name',)
    ordering = ('developer_name',)
