from django.shortcuts import render

# Create your views here.


def index(request):
    """Домашняя страница приложения Blog"""
    return render(request, 'Blog/index.html')