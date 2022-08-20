from rest_framework import serializers
from genres.models import Genre
from genres.serializers import GenreSerializer
from .models import Movie


class MovieSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    premiere = serializers.DateField()
    duration = serializers.CharField(max_length=10)
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()

    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict):
        genres_data = validated_data.pop("genres")

        new_movie = Movie.objects.create(**validated_data)

        for genre in genres_data:
            new_genre, _ = Genre.objects.get_or_create(**genre)
            new_movie.genres.add(new_genre)

        new_movie.save()

        return new_movie

    def update(self, instance, validated_data):
        instance.genres.clear()
        for key, value in validated_data.items():
            if key == "genres":
                for valor in value:
                    genre, _ = Genre.objects.get_or_create(**valor)
                    instance.genres.add(genre)
            else:   
                setattr(instance, key, value)

        instance.save()

        return instance


# EOF
