from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from StraightRate_2.media.models import Movie
from StraightRate_2.reviews.models import MovieReview

UserModel = get_user_model()


class TestMovieDetailsViewIntegration(TestCase):
    def setUp(self):
        self.credentials = {
            "username": "test",
            "email": "testuser@test.com",
            "password": "12admin45"
        }
        self.user = UserModel.objects.create_user(**self.credentials)
        self.movie = Movie.objects.create(
            poster='test',
            title="Test Movie",
            description="Test Description",
            release_date="2023-01-01",
            approved=True
        )

    def test__get_context_data__authenticated_user_with_review__sets_correct_user_review_id(self):
        review = MovieReview.objects.create(
            movie=self.movie,
            user=self.user,
            rating=5,
            comment="Great movie!"
        )
        self.client.login(username=self.credentials['username'], password=self.credentials['password'])

        response = self.client.get(reverse('details-movie', kwargs={'pk': self.movie.pk}))

        self.assertEqual(response.context['user_review_id'], review.id)

    def test__get_context_data__authenticated_user_without_review__sets_user_review_id_to_zero(self):
        self.client.login(username=self.credentials['username'], password=self.credentials['password'])

        response = self.client.get(reverse('details-movie', kwargs={'pk': self.movie.pk}))

        self.assertEqual(response.context['user_review_id'], 0)

    def test__get_context_data__unauthenticated_user__sets_user_review_id_to_zero(self):
        response = self.client.get(reverse('details-movie', kwargs={'pk': self.movie.pk}))

        self.assertEqual(response.context['user_review_id'], 0)
