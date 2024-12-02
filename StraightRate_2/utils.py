from django.contrib.auth.models import Group
from django.db.models import Count
from StraightRate_2.reviews.models import MovieReview, VideoGameReview

PROPOSER_POINTS = 500
REDACTOR_POINTS = 5000


def update_user_groups(user):
    proposer_group, _ = Group.objects.get(name="Proposer")
    redactor_group, _ = Group.objects.get(name="Redactor")

    if user.points >= REDACTOR_POINTS:
        user.groups.add(redactor_group, proposer_group)
    elif user.points >= PROPOSER_POINTS:
        user.groups.add(proposer_group)
        user.groups.remove(redactor_group)
    else:
        user.groups.remove(proposer_group, redactor_group)

    user.save()


def calculate_user_points(user):
    movie_reviews = MovieReview.objects.filter(user=user)
    game_reviews = VideoGameReview.objects.filter(user=user)

    movie_reviews_count = MovieReview.objects.filter(user=user).count()
    game_reviews_count = VideoGameReview.objects.filter(user=user).count()

    review_points = (game_reviews_count + movie_reviews_count) * 5

    like_points = movie_reviews.aggregate(total_likes=Count('likes'))['total_likes'] or 0
    like_points += game_reviews.aggregate(total_likes=Count('likes'))['total_likes'] or 0
    like_points *= 10

    total_points = review_points + like_points

    user.points = total_points
    user.save()

    return total_points
