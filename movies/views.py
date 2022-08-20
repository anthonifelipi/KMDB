from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination

from rest_framework.authentication import TokenAuthentication

from .models import Movie
from .serializers import MovieSerializer
from .permissions import AcessMovies


class MoviesView(APIView, PageNumberPagination):

    authentication_classes = [TokenAuthentication]
    permission_classes = [AcessMovies]

    def get(self, request: Request):
        movies = Movie.objects.all()
        pages = self.paginate_queryset(movies, request)
        movies_serializer = MovieSerializer(pages, many=True)

        return self.get_paginated_response(movies_serializer.data)

    def post(self, request: Request) -> Response:
        movie = MovieSerializer(data=request.data)
        movie.is_valid(raise_exception=True)

        movie.save()

        return Response(movie.data, status.HTTP_201_CREATED)


class MovieByIdView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [AcessMovies]

    def get(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie_serializer = MovieSerializer(movie)

        return Response(movie_serializer.data)

    def delete(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)

        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        movie_serializer = MovieSerializer(movie, data=request.data, partial=True)
        movie_serializer.is_valid(raise_exception=True)

        movie_serializer.save()

        return Response(movie_serializer.data)
