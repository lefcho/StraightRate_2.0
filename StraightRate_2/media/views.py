from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from StraightRate_2.media.forms import MovieCreateForm, VideoGameCreateForm
from StraightRate_2.media.models import Movie, VideoGame
from StraightRate_2.media.serializers import MovieSerializer


class MovieRetrieveAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'movies/suggest-movie.html'
    form_class = MovieCreateForm
    model = Movie
    success_url = reverse_lazy('view-profile')


class VideoGameCreateView(LoginRequiredMixin, CreateView):
    template_name = 'video-games/suggest-video-game.html'
    form_class = VideoGameCreateForm
    model = VideoGame
    success_url = reverse_lazy('view-profile')


class MovieListApproveView(LoginRequiredMixin, ListView):
    template_name = 'movies/movies-approve.html'
    context_object_name = 'movies'
    paginate_by = 2
    model = Movie

    def get_queryset(self):
        return self.model.objects.filter(approved=False).order_by('-date_added')


class VideoGamesListApproveView(LoginRequiredMixin, ListView):
    template_name = 'video-games/video-game-approve.html'
    context_object_name = 'games'
    paginate_by = 1
    model = VideoGame

    def get_queryset(self):
        return self.model.objects.filter(approved=False).order_by('-date_added')


@login_required
def approve_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.approved = True
    movie.save()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def approve_game(request, pk):
    game = VideoGame.objects.get(pk=pk)
    game.approved = True
    game.save()

    return redirect(request.META.get('HTTP_REFERER'))


class MovieByGenreView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/movies-by-genre.html'
    paginate_by = 1

    def get_queryset(self):
        genre = self.kwargs['genre'].lower()
        return self.model.objects.filter(genres__genre_name__iexact=genre)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['genre'] = self.kwargs['genre']
        return context


class VideoGameByGenreView(ListView):
    model = VideoGame
    context_object_name = 'games'
    template_name = 'video-games/video-games-by-genre.html'
    paginate_by = 1

    def get_queryset(self):
        genre = self.kwargs['genre'].lower()
        return self.model.objects.filter(genres__genre_name__iexact=genre)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['genre'] = self.kwargs['genre']
        return context


# class MovieDetailView(DetailView):
#     model = Movie
#     template_name = 'movies/movie-details.html'
#     context_object_name = 'movie'
#     pk_url_kwarg = 'movie_id'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['reviews'] = self.object.reviews.all()
#         context['user_review'] = None
#         context['form'] = None
#
#         if self.request.user.is_authenticated:
#             context['user_review'] = self.object.reviews.filter(user=self.request.user).first()
#
#         return context


# def details_movie_view(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     reviews = movie.reviews.all()
#     user_review = None
#     form = None
#
#     if request.user.is_authenticated:
#         user_review = MovieReview.objects.filter(movie=movie, user=request.user).first()
#
#         if request.method == 'POST':
#             form = AddMovieReviewForm(request.POST, instance=user_review)
#             if form.is_valid():
#                 review = form.save(commit=False)
#                 review.movie = movie
#                 review.user = request.user
#                 review.rating = request.POST.get('rating')
#                 review.save()
#                 return redirect('details-movie', movie_id=movie_id)
#         else:
#             form = AddMovieReviewForm(instance=user_review)
#
#     context = {
#         'movie': movie,
#         'reviews': reviews,
#         'user_review': user_review,
#         'form': form,
#     }
#     return render(request, 'movies/movie-details.html', context)


# class VideoGameDetailView(DetailView):
#     model = VideoGame
#     template_name = 'video-games/video-games-details.html'
#     context_object_name = 'game'
#     pk_url_kwarg = 'game_id'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['reviews'] = self.object.reviews.all()
#         context['user_review'] = None
#         context['form'] = None
#
#         if self.request.user.is_authenticated:
#             context['user_review'] = self.object.reviews.filter(user=self.request.user).first()
#
#         return context
