from django.shortcuts import render
from .models import Blog_News
# Create your views here.
def view_news(request):
    posts=Blog_News.objects.all()
    
    return render(request,'list_news.html',
                  {"posts":posts})
