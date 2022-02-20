"""Определяет схемы URL для Blog"""

from django.urls import path

from . import views

app_name = "Blog"
urlpatterns = [
    # Домашняя страница
    path('', views.posts, name='index'),
    path('create_post/', views.create_post, name='create_post'),
]