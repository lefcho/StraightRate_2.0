from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import MovieReview, VideoGameReview
from .serializers import MovieReviewSerializer, VideoGameReviewSerializer
from ..common.models import MovieReviewLike, VideoGameReviewLike


class ReviewPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10


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


class MovieReviewListView(ListAPIView):
    serializer_class = MovieReviewSerializer
    pagination_class = ReviewPagination

    def get_queryset(self):
        movie_id = self.kwargs.get('movie_id')
        return MovieReview.objects.filter(movie_id=movie_id)


class VideoGameReviewListView(ListAPIView):
    serializer_class = VideoGameReviewSerializer
    pagination_class = ReviewPagination

    def get_queryset(self):
        game_id = self.kwargs.get('game_id')
        return VideoGameReview.objects.filter(game_id=game_id)


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


class VideoGameReviewLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk=None):
        review = get_object_or_404(VideoGameReview, pk=pk)
        user = request.user

        like, created = VideoGameReviewLike.objects.get_or_create(user=user, video_game_review=review)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        return Response({
            'liked': liked,
            'like_count': review.likes.count()
        })
