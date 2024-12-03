from django.db import models
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'o numero minimo é 0'),
            MaxValueValidator(5, 'o numero maximo é 5')
        ],
    )
    comments = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.movie)
