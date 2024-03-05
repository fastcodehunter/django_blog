import string
from django.shortcuts import render, get_object_or_404
from .models import News
from django.core.paginator  import Paginator

def view_news(request):
    posts=News.objects.all()
    paginator=Paginator(posts,2)
    page_number = request.GET.get('page', 0)
    page=paginator.get_page(page_number)
    return render(request,'list_news/list_news.html',
                                                    {"page":page})


def post_detail(request, iid, slug):
    post = get_object_or_404(News, id=iid, slug=slug)
    subsections = post.subsections.all()
    context = {
        'post': post,
        'subsections': subsections,
    }
    return render(request, 'list_news/blog/detail_blog.html', context)








