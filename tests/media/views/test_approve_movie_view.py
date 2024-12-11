from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from StraightRate_2.media.models import Movie

UserModel = get_user_model()


class TestApproveMovieView(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username="testuser",
            email="testuser@test.com",
            password="12admin34"
        )

        self.movie = Movie.objects.create(
            poster="test",
            title="Test Movie",
            description="Test description",
            release_date="2023-01-01",
            approved=False
        )

        self.url = reverse('approve-movie', kwargs={'pk': self.movie.pk})

    def test_user_without_permission_is_redirected(self):
        self.client.login(username="testuser", password="12admin34")

        response = self.client.get(self.url)

        self.assertRedirects(response, f'/?next=/media/approve-movies/{self.movie.pk}/')

        self.movie.refresh_from_db()
        self.assertFalse(self.movie.approved)

    def test_user_with_permission_can_approve_movie(self):
        permission = Permission.objects.get(codename='can_approve_movies', content_type__app_label='media')
        self.user.user_permissions.add(permission)

        self.client.login(username="testuser", password="12admin34")

        response = self.client.get(self.url)

        self.assertRedirects(response, reverse('approve-list-movies'))

        self.movie.refresh_from_db()
        self.assertTrue(self.movie.approved)

