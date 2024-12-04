from django.urls import path
from StraightRate_2.media import views

urlpatterns = [
    path('movies/<int:pk>/', views.MovieRetrieveAPIView.as_view(), name='details-movie'),
    path('suggest-movie/', views.MovieCreateView.as_view(), name='suggest-movie'),
    path('suggest-video-game/', views.VideoGameCreateView.as_view(), name='suggest-game'),
    path('approve-movies/', views.MovieApproveView.as_view(), name='approve-movies'),
]