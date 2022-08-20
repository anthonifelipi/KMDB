from django.urls import path
from . import views


urlpatterns = [
    path("movies/<int:movie_id>/reviews/", views.ReviewView.as_view(), name="reviews"),
    path("movies/<int:movie_id>/reviews/<int:review_id>", views.ReviewBiIdView.as_view(), name="reviews"),
]
