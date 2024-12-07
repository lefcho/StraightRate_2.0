from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import MovieReview, VideoGameReview
from .serializers import MovieReviewSerializer, VideoGameReviewSerializer
from ..common.models import MovieReviewLike


class MovieReviewListCreateView(ListCreateAPIView):
    serializer_class = MovieReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):

        movie_id = self.kwargs.get('movie_id')
        if not movie_id:
            raise ValidationError({"error": "Movie ID is required"})
        return MovieReview.objects.filter(movie_id=movie_id)


class VideoGameReviewListCreateView(ListCreateAPIView):
    serializer_class = VideoGameReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):

        game_id = self.kwargs.get('game_id')
        if not game_id:
            raise ValidationError({"error": "Video game ID is required"})
        return VideoGameReview.objects.filter(game_id=game_id)


# Retrieve, Update, Delete a Movie Review
class MovieReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this review.")
        serializer.save()


class VideoGameReviewDetailView(RetrieveUpdateDestroyAPIView):
    queryset = VideoGameReview.objects.all()
    serializer_class = VideoGameReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this review.")
        serializer.save()


# Like or Unlike a Review
class MovieReviewLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk=None):
        review = get_object_or_404(MovieReview, pk=pk)
        user = request.user

        like, created = MovieReviewLike.objects.get_or_create(user=user, movie_review=review)
        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        return Response({
            'liked': liked,
            'like_count': review.likes.count()
        })
