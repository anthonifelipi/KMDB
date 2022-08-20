from django.urls import path
from . import views


urlpatterns = [
    path("movies/", views.MoviesView.as_view(), name="movies"),
    path("movies/<int:movie_id>", views.MovieByIdView.as_view(), name="movies_id"),
]
