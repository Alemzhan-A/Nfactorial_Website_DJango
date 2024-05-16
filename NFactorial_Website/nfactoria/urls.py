from django.urls import path
from . import views


urlpatterns = [
    path('musics/', views.musics, name='musics'),
    path('musics/<int:id>', views.musicpost,name='musicpost'),
    path('login', views.login,name='login'),
    path('signup', views.signup,name='signup'),
    path('search', views.search, name='search'),
    path('search_by_genre', views.search_by_genre, name='search_by_genre')
]
