from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.url import blog_urls
from profil.url import urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(blog_urls)),
    path('',include(urlpatterns))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)