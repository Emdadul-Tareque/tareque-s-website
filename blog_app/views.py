from django.http import HttpRequest
from django.shortcuts import render
from blog_app.models import Blog, Category


def index(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog
    }

    return render(request, 'index.html', context)


def blog_view(request, pk):
    post = Blog.objects.get(pk=pk)
    print(post)
    context = {
        'post': post
    }

    return render(request, "blog.html", context)


def all_blog(request: HttpRequest):
    blog = Blog.objects.all()
    if 'category' in request.GET:
        category = int(request.GET.get('category'))
        blog = blog.filter(category=category)
    category = Category.objects.all()
    context = {
        'blog': blog.order_by('-created_at'),
        'category': category
    }

    return render(request, 'all_blog.html', context)
