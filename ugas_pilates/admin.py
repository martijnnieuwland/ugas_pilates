# ugas_pilates/admin.py
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

class CustomAdminSite(admin.AdminSite):
    site_header = "Uga’s Pilates Administration"
    site_title = "Uga’s Pilates"
    index_title = "Dashboard"

    def get_app_list(self, request, app_label=None):
        """
        Custom ordering of apps and models in the admin index.
        """
        app_order = ["pages", "blog"]
        model_order = {
            "pages": ["Instructor", "Pricelist", "PricelistItem"],
            "blog": ["Post"],
        }

        app_list = super().get_app_list(request, app_label=None)

        # Sort apps
        app_list.sort(
            key=lambda app: app_order.index(app["app_label"])
            if app["app_label"] in app_order
            else 999
        )

        # Sort models within apps
        for app in app_list:
            if app["app_label"] in model_order:
                app["models"].sort(
                    key=lambda m: model_order[app["app_label"]].index(m["object_name"])
                    if m["object_name"] in model_order[app["app_label"]]
                    else 999
                )

        return app_list


# Create a single global instance
custom_admin_site = CustomAdminSite(name="custom_admin")

# Register Django’s built-in auth models
custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Group, GroupAdmin)
