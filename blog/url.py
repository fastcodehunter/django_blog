from django.urls import path
from blog import views
from django.contrib.auth.views import LogoutView

app_name = 'blog'

blog_urls = [
    path("",views.view_news,name='list_blog'),
    path("", LogoutView.as_view(), name='logout'),
    path('post/<int:iid>/<slug:slug>/', views.post_detail, name='post_detail'),

]
