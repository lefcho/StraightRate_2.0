from django.shortcuts import render
from django.views.generic import DetailView

from StraightRate_2.media.models import Movie


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie-details.html'
    context_object_name = 'movie'
    pk_url_kwarg = 'movie_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['reviews'] = self.object.reviews.all()
        context['user_review'] = None
        context['form'] = None

        if self.request.user.is_authenticated:
            context['user_review'] = self.object.reviews.filter(user=self.request.user).first()

        return context


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
