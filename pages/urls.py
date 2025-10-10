from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("studio/", views.studio, name="studio"),
    path("instructors/", views.instructors, name="instructors"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("faq/", views.faq, name="faq"),
    path("schedule/", views.schedule, name="schedule"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
    path("privacy-policy/", views.privacy, name="privacy"),
    path("terms-of-service/", views.terms, name="terms"),
]
