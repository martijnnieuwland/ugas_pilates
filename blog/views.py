from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/index.html", context=context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, "blog/detail.html", context)
