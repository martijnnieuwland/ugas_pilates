from django.contrib import admin
from ugas_pilates.admin import custom_admin_site
from .models import Post

@admin.register(Post, site=custom_admin_site)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "published"]
    search_fields = ["title"]
