from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blog_id>', views.blog_post, name='blog_post'),
]
