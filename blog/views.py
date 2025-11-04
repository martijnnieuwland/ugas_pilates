from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts,
               "title": "Uga's Blog",
                "heading": "True to the Core!",
                "seo": "All about True Pilates in Antwerp, Belgium",}
    return render(request, "blog/index.html", context=context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {"post": post,
               "title": "Uga's Blog",
                "heading": post.title,
                "seo": "All about True Pilates in Brasschaat, Belgium",}
    return render(request, "blog/detail.html", context)
