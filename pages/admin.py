from django.contrib import admin
from ugas_pilates.admin import custom_admin_site
from .models import Instructor, Pricelist, PricelistItem, Studio


class PricelistItemInline(admin.TabularInline):
    model = PricelistItem
    extra = 1
    min_num = 0
    can_delete = True


@admin.register(Instructor, site=custom_admin_site)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Pricelist, site=custom_admin_site)
class PricelistAdmin(admin.ModelAdmin):
    list_display = ('category',)
    inlines = [PricelistItemInline]


@admin.register(Studio, site=custom_admin_site)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('caption',)
    search_fields = ('caption',)
