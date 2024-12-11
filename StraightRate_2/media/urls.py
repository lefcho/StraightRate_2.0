from django.urls import path
from StraightRate_2.media import views

urlpatterns = [
    path('movies/<int:pk>/', views.MovieDetailsView.as_view(), name='details-movie'),
    path('video-games/<int:pk>/', views.VideoGameDetailsView.as_view(), name='details-games'),
    path('suggest-movie/', views.MovieCreateView.as_view(), name='suggest-movie'),
    path('suggest-video-game/', views.VideoGameCreateView.as_view(), name='suggest-game'),
    path('approve-list-movies/', views.MovieListApproveView.as_view(), name='approve-list-movies'),
    path('approve-list-video-games/', views.VideoGamesListApproveView.as_view(), name='approve-list-games'),
    path('approve-movies/<int:pk>/', views.approve_movie, name='approve-movie'),
    path('approve-video-game/<int:pk>/', views.approve_game, name='approve-game'),
    path('movies/genre/<str:genre>/', views.MovieByGenreView.as_view(), name='movies-by-genre'),
    path('video-games/genre/<str:genre>/', views.VideoGameByGenreView.as_view(), name='games-by-genre'),
    path('all-movies/', views.AllMoviesView.as_view(), name='all-movies'),
    path('all-video-games/', views.AllVideoGamesView.as_view(), name='all-games'),

]
