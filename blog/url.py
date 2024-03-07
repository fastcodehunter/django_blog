from django.urls import path
from blog import views

app_name = 'blog'

blog_urls = [
    path("",views.view_news,name='list_blog'),
    path('post/<int:iid>/<slug:slug>/', views.post_detail, name='post_detail'),
]