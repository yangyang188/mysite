from django.urls import path
from . import views

# start with blog
urlpatterns = [
    # http://localhost:800/blog/1
    path('', views.blog_list, name='blog_list'),  # 博客列表
    path('<int:blog_pk>', views.blog_detail, name='blog_detail'),  # 博客内容
    path('type/<int:blog_type_pk>', views.blogs_with_type, name='blogs_with_type'),  # 博客分类
    path('date/<int:year>/<int:month>', views.blogs_with_date, name='blogs_with_date'),  # 日期分类
]
