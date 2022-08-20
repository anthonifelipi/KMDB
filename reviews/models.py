from email import message
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class RecomendationChoices(models.TextChoices):
    HIGH = "Must Watch"
    MEDIUM = "Should Watch"
    LOW = "Avoid Watch"
    DEFAULT = "No Opinion"


class Review(models.Model):
    stars = models.IntegerField(
        validators=[MaxValueValidator(10), MinValueValidator(1)],
    )
    review = models.TextField()
    spoilers = models.BooleanField(null=True, blank=True, default=False)
    recomendation = models.CharField(
        max_length=50,
        choices=RecomendationChoices.choices,
        default=RecomendationChoices.DEFAULT,
    )

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )

    user = models.ForeignKey(
        "custom_user.CustomUser", on_delete=models.CASCADE, related_name="reviews"
    )


# EOF
