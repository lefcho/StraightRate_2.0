from django.urls import path
from .views import MovieRetrieveAPIView

urlpatterns = [
    path('movies/<int:pk>/', MovieRetrieveAPIView.as_view(), name='details-movie'),
]