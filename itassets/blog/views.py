from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from blog.models import Post


def index(request):
    posts = Post.objects.all()
    return render('blog/index.html', {'posts': posts})


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render('blog/post.html', {'post': post})
