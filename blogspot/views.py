from django.shortcuts import render
from . import models


def index(request, template='index.html', ajax='index_entries.html'):
    blog = models.Blog.objects.get()
    all_posts = models.Post.objects.all().order_by("-created")
    if request.is_ajax():
        template = ajax
    return render(request, template, {'posts': all_posts, 'blog': blog},)


def post(request, slug):
    single_post = models.Post.objects.get(slug=slug)
    return render(request, 'post.html', {'post': single_post},)
