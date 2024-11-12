from django.db import models


class AbstractGenre(models.Model):
    class Meta:
        abstract = True

    genre_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genre_name


class VideoGameGenre(AbstractGenre):
    pass


class MovieGenre(AbstractGenre):
    pass
