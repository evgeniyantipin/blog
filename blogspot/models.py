from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    slug = models.SlugField(default="", unique=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.body