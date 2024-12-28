from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('help', views.help),
    path('about', views.about),
    path('map', views.map),
    path('login', views.login),
    path('games', views.games),
    path('signup', views.signup),
    path('login1', views.user_login, name='login1'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)