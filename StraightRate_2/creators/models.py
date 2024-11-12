from django.db import models


class Director(models.Model):
    first_name = models.CharField(
        max_length=150,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=150,
        verbose_name='Last Name',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Developer(models.Model):
    developer_name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Developer Name',
    )

    website = models.URLField(
        null=True,
        blank=True,
        verbose_name='Website',
    )

    def __str__(self):
        return self.developer_name
