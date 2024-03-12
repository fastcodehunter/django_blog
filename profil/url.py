from django.urls import path
from .views import SignUpView,sing_in,view_profil
from django.conf.urls.static import static
from django.conf import settings
from blog import views
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
app_name = 'profil'

urlpatterns = [
    path("", views.view_news, name='list_blog'),
    path('sing-up/', SignUpView.as_view(), name="Sing Up"),
    path('sing-in/', sing_in, name="Sing In"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profil/<int:id_author>/<slug:name__author>/',view_profil,name='profil')
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)