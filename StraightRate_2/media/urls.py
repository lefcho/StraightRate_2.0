from django.urls import path

from StraightRate_2.media import views

urlpatterns = (
    path('<int:movie_id>/details-movie/',
         views.MovieDetailView.as_view(),
         name='details-movie'),
    path('<int:game_id>/details-game/',
         views.VideoGameDetailView.as_view(),
         name='details-game'),

)
