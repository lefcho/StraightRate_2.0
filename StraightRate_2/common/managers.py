from django.db.models import Count, Manager


class ReviewManager(Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            like_count=Count('likes')
        ).order_by('-like_count')
