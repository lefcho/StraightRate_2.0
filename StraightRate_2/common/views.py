from django.views.generic import TemplateView
from django.db.models import Avg, Count
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
