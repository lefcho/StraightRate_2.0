from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from StraightRate_2.media.forms import MovieCreateForm, VideoGameCreateForm
from StraightRate_2.media.models import Movie, VideoGame
from StraightRate_2.reviews.models import MovieReview, VideoGameReview


class MovieDetailsView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movies/movie-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_review = MovieReview.objects.filter(movie=self.object, user=self.request.user).first()
        if user_review:
            context['user_review_id'] = user_review.id
        else:
            context['user_review_id'] = 0
        return context


class VideoGameDetailsView(DetailView):
    model = VideoGame
    context_object_name = 'game'
    template_name = 'video-games/video-games-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_review = VideoGameReview.objects.filter(game=self.object, user=self.request.user).first()
        if user_review:
            context['user_review_id'] = user_review.id
        else:
            context['user_review_id'] = 0
        return context


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'movies/suggest-movie.html'
    form_class = MovieCreateForm
    model = Movie
    success_url = reverse_lazy('view-profile')
    permission_required = 'media.can_suggest_movies'

    def handle_no_permission(self):
        return redirect('home')


class VideoGameCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'video-games/suggest-video-game.html'
    form_class = VideoGameCreateForm
    model = VideoGame
    success_url = reverse_lazy('view-profile')
    permission_required = 'media.can_suggest_games'

    def handle_no_permission(self):
        return redirect('home')


class MovieListApproveView(PermissionRequiredMixin, ListView):
    template_name = 'movies/movies-approve.html'
    context_object_name = 'movies'
    paginate_by = 5
    model = Movie
    permission_required = 'media.can_approve_movies'

    def get_queryset(self):
        return self.model.objects.filter(approved=False).order_by('-date_added')

    def handle_no_permission(self):
        return redirect('home')


class VideoGamesListApproveView(PermissionRequiredMixin, ListView):
    template_name = 'video-games/video-game-approve.html'
    context_object_name = 'games'
    paginate_by = 5
    model = VideoGame
    permission_required = 'media.can_approve_games'

    def get_queryset(self):
        return self.model.objects.filter(approved=False).order_by('-date_added')

    def handle_no_permission(self):
        return redirect('home')


@login_required
@permission_required('media.can_approve_movies', login_url='home')
def approve_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.approved = True
    movie.save()

    return redirect('approve-list-movies')


@login_required
@permission_required('media.can_approve_games', login_url='home')
def approve_game(request, pk):
    game = VideoGame.objects.get(pk=pk)
    game.approved = True
    game.save()

    return redirect('approve-list-games')


class MovieByGenreView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/movies-by-genre.html'
    paginate_by = 5

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
    paginate_by = 5

    def get_queryset(self):
        genre = self.kwargs['genre'].lower()
        return self.model.objects.filter(genres__genre_name__iexact=genre)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['genre'] = self.kwargs['genre']
        return context


class AllMoviesView(ListView):
    model = Movie
    context_object_name = 'movies'
    paginate_by = 20
    template_name = 'movies/all-movies.html'


class AllVideoGamesView(ListView):
    model = VideoGame
    context_object_name = 'games'
    paginate_by = 20
    template_name = 'video-games/all-video-games.html'
