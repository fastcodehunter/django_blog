from django.shortcuts import render

# Create your views here.
def view_blog(request):
    return render(request,'list_news.html')
