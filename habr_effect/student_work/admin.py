from django.contrib import admin

# Register your models here.

from .models import Dip_work


class Dip_workAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'writer', 'is_published')


admin.site.register(Dip_work, Dip_workAdmin)