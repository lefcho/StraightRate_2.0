from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_id>/', views.MovieReviewListCreateView.as_view(), name='movie-review-list-create'),
    path('movie-review/<int:pk>/', views.MovieReviewDetailView.as_view(), name='movie-review-detail'),
    path('like/movie-review/<int:pk>/', views.MovieReviewLikeView.as_view(), name='movie-review-like'),
    path('games/<int:game_id>/', views.VideoGameReviewListCreateView.as_view(), name='game-review-list-create'),
    path('game-review/<int:pk>/', views.VideoGameReviewDetailView.as_view(), name='movie-review-detail'),
    path('movie-reviews/<int:movie_id>/', views.MovieReviewListView.as_view(), name='paginated-movie-reviews'),
]