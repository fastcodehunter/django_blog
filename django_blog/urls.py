from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.url import product_patterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(product_patterns))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)