from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_id>/', views.MovieReviewListCreateView.as_view(), name='movie-review-list-create'),
    path('<int:pk>/', views.MovieReviewDetailView.as_view(), name='movie-review-detail'),
    path('<int:pk>/like/', views.MovieReviewLikeView.as_view(), name='movie-review-like'),
]