from django.http import HttpRequest
from django.shortcuts import render



def blog(request):
    return render(request, 'ugas_pilates/blog.html')

def contact(request):
    return render(request, 'ugas_pilates/contact.html')

def faq(request):
    return render(request, 'ugas_pilates/faq.html')

def home(request):
    return render(request, 'ugas_pilates/home.html')

def index(request):
    return render(request, 'ugas_pilates/index.html')

def instructors(request):
    return render(request, 'ugas_pilates/instructors.html')

def pricing(request):
    return render(request, 'ugas_pilates/pricing.html')

def schedule(request):
    return render(request, 'ugas_pilates/schedule.html')

def testimonials(request):
    return render(request, 'ugas_pilates/testimonials.html')

def ugas(request):
    return render(request, 'ugas_pilates/ugas.html')
