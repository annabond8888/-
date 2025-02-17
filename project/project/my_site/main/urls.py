from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    path('help', views.help),
    path('about-us', views.abo, name='abo'),
    path('map', views.map),
    path('games', views.games),
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('task', views.fill_the_gaps, name='task'),
    path('question', views.questions, name='question'),
    path('cards', views.flashcards, name='flashcards'),
    path('entertest', views.test_view, name='test'),
    path('submit/', views.submit_answers, name='submit_answers'),
    path('result/<str:result>/', views.result_view, name='result'),
    path('check-choice/', views.check_choice, name='check_choice'),
    path('check-answer/', views.check_answer, name='check_answer'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)