import os

from django.shortcuts import render


def contact(request):
    context = {
        "title": "Contact",
        "heading": "Get in Touch",
        "seo": "10 minutes from Antwerp",
        "GM_KEY": os.getenv("GM_KEY"),
    }
    return render(request, "pages/contact.html", context)


def faq(request):
    context = {
        "title": "FAQ",
        "heading": "Frequently Asked Questions",
        "seo": "10 commom questions about True Pilates",
    }
    return render(request, "pages/faq.html", context)


def home(request):
    context = {
        "title": "Uga's Pilates - True Pilates",
        "heading": "True to the core" "",
    }
    return render(request, "pages/index.html", context)


def instructors(request):
    context = {
        "title": "Instructors",
        "heading": "Meet Your Instructor",
        "seo": "Dedicated to your wellbeing",
    }
    return render(request, "pages/instructors.html", context)


def pricing(request):
    context = {
        "title": "Pricing",
        "heading": "Your Value",
        "seo": "Train for only €20",
    }
    return render(request, "pages/pricing.html", context)


def privacy(request):
    context = {
        "title": "Privacy Policy",
        "heading": "Privacy Policy",
    }
    return render(request, "pages/privacy-policy.html", context)


def schedule(request):
    context = {
        "title": "Schedule",
        "heading": "Studio Opening Hours",
        "seo": "Flexible hours to accomodate your schedule",
    }
    return render(request, "pages/schedule.html", context)


def studio(request):
    context = {
        "title": "Uga's Pilates",
        "heading": "The Studio",
        "seo": "Following Romana Kryzanowska's true pilates method",
    }
    return render(request, "pages/studio.html", context)


def terms(request):
    context = {
        "title": "Terms of Service",
        "heading": "Terms of Service",
    }
    return render(request, "pages/terms-of-service.html", context)


def testimonials(request):
    context = {
        "title": "Testimonials",
        "heading": "Hear it from our hard core!",
        "seo": "Why our customers choose us",
    }
    return render(request, "pages/testimonials.html", context)
