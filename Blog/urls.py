"""Определяет схемы URL для Blog"""

from django.urls import path

from . import views

app_name = "Blog"
urlpatterns = {
    # Домашняя страница
    path('', views.index, name='index'),
    path('', views.posts, name='posts')
}