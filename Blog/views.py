from django.shortcuts import render, redirect
from django.views import generic
from django.http import Http404

from django.contrib.auth.decorators import login_required
from Blog .models import BlogPost
from .forms import BlogForm
# Create your views here.


def posts(request):
    """Выводит список постов"""
    posts = BlogPost.objects.all().order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'Blog/index.html', context)


def post(request, post_id):
    """Выводит одну тему и все ее записи"""
    post = BlogPost.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'Blog/post.html', context)


@login_required
def create_post(request):
    """Создает новый пост"""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            create_post = form.save(commit=False)
            create_post.owner = request.user
            create_post.save()
            return redirect('Blog:index')

    context = {'form': form}
    return render(request, 'Blog/create_post.html', context)


@login_required
def edit_post(request, post_id):
    """Редактирует существующую запись."""
    edit = BlogPost.objects.get(id=post_id)
    if edit.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = BlogForm(instance=edit)
    else:
        form = BlogForm(instance=edit, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Blog:post', post_id=edit.id)
    context = {'edit': edit, 'form': form}
    return render(request, 'Blog/edit_post.html', context)