from django.urls import path
from blog import views

app_name = 'blog'

product_patterns = [
    path("",views.view_news,name='list_blog'),
    path('post/<int:iid>/<slug:slug>/', views.post_detail, name='post_detail'),
]