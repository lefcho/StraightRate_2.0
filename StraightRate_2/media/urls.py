from django.urls import path

from StraightRate_2.media import views

urlpatterns = (
    path('<int:movie_id>/details-movie/', views.MovieDetailView.as_view(), name='details-movie'),
)
