from django.db.models.functions import Concat
from django.views.generic import TemplateView
from django.db.models import Avg, Count, Value, Q

from StraightRate_2.creators.models import Developer, Director
from StraightRate_2.media.models import Movie, VideoGame


class HomeView(TemplateView):
    template_name = 'common/home.html'

    @staticmethod
    def get_top_rated_items(model, limit=5):
        return (model.objects
                .annotate(avg_rating=Avg('reviews__rating'), review_count=Count('reviews'))
                .filter(review_count__gt=0, approved=True)
                .order_by('-avg_rating')[:limit])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_movies'] = self.get_top_rated_items(Movie)
        context['top_games'] = self.get_top_rated_items(VideoGame)
        return context


class SearchedMediaView(TemplateView):
    template_name = 'common/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')

        directors = Director.objects.annotate(
            full_name=Concat('first_name', Value(' '), 'last_name')
        ).filter(Q(full_name__icontains=query))

        developers = Developer.objects.filter(developer_name__icontains=query)

        if len(query) == 1:
            movie_results = Movie.objects.filter(title__istartswith=query)
            game_results = VideoGame.objects.filter(title__istartswith=query)
        else:
            movie_results = Movie.objects.filter(title__icontains=query)
            game_results = VideoGame.objects.filter(title__icontains=query)

        context.update({
            'query': query,
            'movie_results': movie_results,
            'game_results': game_results,
            'directors': directors,
            'developers': developers,
        })

        return context
