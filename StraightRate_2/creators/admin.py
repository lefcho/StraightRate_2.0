from django.contrib import admin
from StraightRate_2.creators.models import Director, Developer


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass
