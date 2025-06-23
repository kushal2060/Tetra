from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('homepage/', views.homepage, name='homepage'),
    path('games/', views.games, name='games'),
    path('flappy-game/', views.flappy_game, name='flappy_game'),
    
    # Add more paths for other pages as needed
]