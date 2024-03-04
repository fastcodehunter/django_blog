from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from django.conf.urls import handler404

app_name = 'news'



product_patterns = [
    path("",views.view_news,name='list_blog'),
   path('post/<int:iid>/<slug:slug>/', views.post_detail, name='post_detail'),
]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(product_patterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)