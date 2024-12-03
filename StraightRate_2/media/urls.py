from django.urls import path

from StraightRate_2.media import views

urlpatterns = [
    path('movies/<int:pk>/', views.MovieRetrieveAPIView.as_view(), name='details-movie'),
    path('suggest-movie/', views.MovieCreateView.as_view(), name='suggest-movie'),
]