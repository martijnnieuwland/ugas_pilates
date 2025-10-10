from django.shortcuts import render


# Not included in urls.  Only for use as playground in project environment -->
def testbed(request):
    context = {
        "title": "Testimonials",
        "heading": "Hear it from our hard core!",
        "seo": "Why our customers choose us",
    }
    return render(request, 'ugas_pilates/testbed.html', context)
