from django.contrib import admin
from .models import Instructor, Pricelist, PricelistItem


# Register your models here.
admin.site.register([Instructor])
admin.site.site_header = "Uga's Pilates Admin"
admin.site.site_title = "Uga's Pilates Admin Portal"
admin.site.index_title = "Welcome to Uga's Pilates Admin"


class PricelistItemInline(admin.TabularInline):
    model = PricelistItem
    extra = 1  # how many empty rows to show for adding new items


@admin.register(Pricelist)
class PricelistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [PricelistItemInline]


@admin.register(PricelistItem)
class PricelistItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'pricelist')
    list_filter = ('pricelist',)
