from django.urls import path
from StraightRate_2.media import views

urlpatterns = [
    path('movies/<int:pk>/', views.MovieRetrieveAPIView.as_view(), name='details-movie'),
    path('suggest-movie/', views.MovieCreateView.as_view(), name='suggest-movie'),
    path('suggest-video-game/', views.VideoGameCreateView.as_view(), name='suggest-game'),
    path('approve-list-movies/', views.MovieListApproveView.as_view(), name='approve-list-movies'),
    path('approve-list-video-games/', views.VideoGamesListApproveView.as_view(), name='approve-list-games'),
    path('approve-movies/<int:pk>/', views.approve_movie, name='approve-movie'),
    path('approve-video-game/<int:pk>/', views.approve_game, name='approve-game'),
]
