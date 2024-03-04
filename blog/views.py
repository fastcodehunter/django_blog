import string
from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import Blog_News,Subsection
import unidecode
from django.http import HttpResponseNotFound

def view_news(request):
    posts=Blog_News.objects.all()
    
    return render(request,'list_news/list_news.html',
                  {"posts":posts})


def post_detail(request, iid, slug):
    post = get_object_or_404(Blog_News, id=iid, slug=slug)
    subsections = post.subsections.all()
    context = {
        'post': post,
        'subsections': subsections,
    }
    return render(request, 'list_news/blog/blog.html', context)








