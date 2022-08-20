from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from movies.models import Movie
from .permissions import AcessReviews, DeleteReview
from .models import Review
from .serializers import ReviewSerializer


class ReviewView(APIView, PageNumberPagination):

    authentication_classes = [TokenAuthentication]
    permission_classes = [AcessReviews]

    def get(self, request: Request, movie_id) -> Response:
        review = Review.objects.filter(movie_id=movie_id)
        pages = self.paginate_queryset(review, request)

        review_serializer = ReviewSerializer(pages, many=True)

        return self.get_paginated_response(review_serializer.data)

    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        check_review = Review.objects.filter(movie=movie, user=request.user).exists()
        if check_review:
            return Response(
                {"Details": "Review already exists."}, status.HTTP_403_FORBIDDEN
            )
        review = ReviewSerializer(data=request.data)
        review.is_valid(raise_exception=True)

        review.save(user=request.user, movie_id=movie_id)

        return Response(review.data, status.HTTP_201_CREATED)


class ReviewBiIdView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [DeleteReview]

    def get(self, request: Request, movie_id: int, review_id: int) -> Response:
        movie = Movie.objects.filter(id=movie_id)
        if not movie:
            return Response({"details": "Movie not found"}, status.HTTP_404_NOT_FOUND)

        review = get_object_or_404(Review, id=review_id)
        review_serializer = ReviewSerializer(review)

        return Response(review_serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int, review_id: int):
        review = get_object_or_404(Review, id=review_id)
        movie = get_object_or_404(Movie, id=movie_id)

        check_movie_review = movie.reviews.filter(id=review_id)

        if not check_movie_review:
            return Response({"details": "Not found"})

        self.check_object_permissions(request, check_movie_review)

        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
