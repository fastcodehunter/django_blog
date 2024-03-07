from django.urls import path
from .views import sing_in, sing_up
from blog import views

app_name = 'profil'

urlpatterns = [
    path("", views.view_news, name='list_blog'),
    path('sing-up/', sing_up, name="Sing Up"),
    path('sing-in/', sing_in, name="Sing In"),
]
