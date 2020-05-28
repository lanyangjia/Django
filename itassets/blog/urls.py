# -*- coding: utf-8 -*-

from django.urls import path, include


# app_name = 'blog'
# urlpatterns = [
#     path('', 'blog.views.index', name='index'),
#     path('', 'blog.views.post', name='post'),
# ]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    # path('ueditor/', include('DjangoUeditor.urls')),
]
