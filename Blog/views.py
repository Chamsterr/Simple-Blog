from django.shortcuts import render, redirect

from Blog .models import BlogPost
from .forms import BlogForm
# Create your views here.


def posts(request):
    """Выводит список постов"""
    posts = BlogPost.objects.all().order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'Blog/index.html', context)


def create_post(request):
    """Создает новый пост"""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blog:index')

    context = {'form': form}
    return render(request, 'Blog/create_post.html', context)