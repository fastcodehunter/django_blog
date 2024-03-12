import string
from django.shortcuts import render, get_object_or_404,redirect
from .models import User,News
from django.core.paginator  import Paginator
from django.contrib.auth.decorators import login_required
from profil.models import Profil





@login_required
def view_news(request):
    posts=News.objects.all()
    paginator=Paginator(posts,1)
    page_number = request.GET.get('page', 0)
    page=paginator.get_page(page_number)
    return render(request,'list_news/list_news.html',
                                                    {"page":page,
                                                     'username': request.user.username})


def view_news(request):
    posts=News.objects.all()
    paginator=Paginator(posts,2)
    page_number = request.GET.get('page', 0)
    page=paginator.get_page(page_number)
    return render(request,'list_news/list_news.html',
                                                    {"page":page,
                                                     'username': request.user.username})




@login_required
def post_detail(request, iid, slug):
    post = get_object_or_404(News, id=iid, slug=slug)
    profils = Profil.objects.get(author=request.user.id)
    subsections = post.subsections.all()
    context = {
        'post': post,
        'subsections': subsections,
    }

    if request.method == "GET":
        if not post.count_viewing.filter(id=profils.id).exists():
            post.count_viewing.add(profils)
    return render(request, 'list_news/blog/detail_blog.html', context)

