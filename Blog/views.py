from django.shortcuts import render
from Blog .models import BlogPost
# Create your views here.


def index(request):
    """Домашняя страница приложения Blog"""
    return render(request, 'Blog/index.html')


def posts(request):
    """Выводит список постов"""
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'Blog/index.html', context)
