from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# from blog_app.write_blog import write
from blog_app.models import Blog


def index(request: HttpRequest):
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

    context = {
        'blog': blog.order_by('-created_at')
    }

    return render(request, 'all_blog.html', context)
