from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from StraightRate_2.media.models import Movie

UserModel = get_user_model()


class TestMovieListApproveView(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username="testuser",
            email="testuser@test.com",
            password="12admin34"
        )

        self.approved_movie = Movie.objects.create(
            poster="test",
            title="Approved Movie",
            description="An approved movie",
            release_date="2023-01-01",
            approved=True
        )

        self.unapproved_movie_1 = Movie.objects.create(
            poster="test",
            title="Unapproved Movie",
            description="An unapproved movie",
            release_date="2023-01-01",
            approved=False
        )

        self.unapproved_movie_2 = Movie.objects.create(
            poster="test",
            title="Unapproved Movie",
            description="An unapproved movie",
            release_date="2023-01-01",
            approved=False
        )

        self.url = reverse('approve-list-movies')

    def test_no_permission_redirects(self):
        UserModel.objects.create_user(
            username="testuser2",
            email="testuser2@test.com",
            password="12admin34"
        )

        self.client.login(username="testuser2", password="12admin34")

        response = self.client.get(self.url)

        self.assertRedirects(response, '/')

    def test_user_with_permission_sees_approved_movies(self):
        permission = Permission.objects.get(codename='can_approve_movies', content_type__app_label='media')
        self.user.user_permissions.add(permission)

        self.client.login(username="testuser", password="12admin34")

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        movies_in_context = response.context['movies']

        self.assertIn(self.unapproved_movie_1, movies_in_context)
        self.assertIn(self.unapproved_movie_2, movies_in_context)
        self.assertNotIn(self.approved_movie, movies_in_context)