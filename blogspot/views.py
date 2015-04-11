from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from .forms import CommentForm


def index(request, template='index.html', ajax='index_entries.html'):
    blog = models.Blog.objects.get()
    all_posts = models.Post.objects.all().order_by("-created")
    if request.is_ajax():
        template = ajax
    return render(request, template, {'posts': all_posts, 'blog': blog},)


def post(request, slug):
    single_post = models.Post.objects.get(slug=slug)

    comment_form = CommentForm(request.POST or None)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = single_post
        comment.save()
    return render(request, 'post.html', {'post': single_post, 'commentform': comment_form},)
