# -*- coding: utf-8 -*-

from django.urls import path


app_name = 'blog'
urlpatterns = [
    path('', 'blog.views.index', name='index'),
    path('', 'blog.views.post', name='post'),
]
