from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator


class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=20,
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(), message="Username already exists"
            )
        ],
    )
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=CustomUser.objects.all(), message="Email already exists"
            ),
        ],
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField()
    bio = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    is_critic = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)
    updated_at = serializers.CharField(read_only=True)

    def create(self, validated_data: dict):
        new_user = CustomUser.objects.create_user(**validated_data)

        new_user.save()

        return new_user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name"]


# EOF
