from django.forms import CharField
from rest_framework import serializers
from reviews.models import Review
from custom_user.serializer import CriticSerializer
from rest_framework.views import Request, View


class ReviewSerializer(serializers.ModelSerializer):

    critic = CriticSerializer(read_only=True, source="user")
    
    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "recomendation",
            "movie_id",
            "critic",
        ]

