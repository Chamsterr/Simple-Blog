"""Определяет схемы URL для Blog"""
from . import views
from django.urls import path

from . import views

app_name = "Blog"
urlpatterns = [
    # Домашняя страница
    path('', views.posts, name='index'),
    path('/<int:post_id>/', views.post, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post',),
]