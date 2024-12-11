from django.test import TestCase
from django.contrib.auth import get_user_model
from StraightRate_2.creators.models import Director
from StraightRate_2.media.models import Movie
from StraightRate_2.reviews.models import MovieReview

UserModel = get_user_model()


class MovieModelTest(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='12admin34'
        )

        self.director = Director.objects.create(
            first_name='Test',
            last_name='Director'
        )

        self.movie = Movie.objects.create(
            title='Test Movie',
            description='A movie for testing.',
            release_date="2023-01-01",
            approved=True,
        )

        self.movie.directors.add(self.director)

    def test_get_average_rating_with_reviews(self):
        MovieReview.objects.create(
            user=self.user,
            movie=self.movie,
            rating=4,
            comment='Great movie!'
        )

        another_user = UserModel.objects.create_user(username='testuser2', password='12admin34')
        MovieReview.objects.create(
            user=another_user,
            movie=self.movie,
            rating=3,
            comment='It was okay.'
        )

        avg_rating = self.movie.get_average_rating()

        self.assertEqual(avg_rating, 3.5)

    def test_get_average_rating_no_reviews(self):
        avg_rating = self.movie.get_average_rating()

        self.assertIsNone(avg_rating)

    def test_movie_str_method(self):
        movie_str = str(self.movie)

        self.assertEqual(movie_str, 'Test Movie')
