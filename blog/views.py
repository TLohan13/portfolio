from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.shortcuts import render, get_object_or_404


def blog(request):
    blog_posts = Blog.objects.order_by('-blog_date')
    return render(request, 'blog.html', {'blog_posts': blog_posts})


def blog_post(request, blog_id):
    blog_post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog_post.html', {'blog_post': blog_post})
