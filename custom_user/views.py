from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from .models import CustomUser
from .permissions import AcessOwnerOrAdmin
from custom_user.serializer import CustomUserSerializer, LoginSerializer


class RegisterCustomView(APIView):
    def post(self, request: Request):
        user = CustomUserSerializer(data=request.data)

        user.is_valid(raise_exception=True)
        user.save()

        return Response(user.data, status.HTTP_201_CREATED)


class LoginWithObtainView(ObtainAuthToken):
    def post(self, request: Request) -> Response:
        login = self.serializer_class(data=request.data, context={"request": request})

        validated_fields = LoginSerializer(data=request.data)
        validated_fields.is_valid(raise_exception=True)

        if not login.is_valid():
            return Response(
                {"details": "Wrong password or username"}, status.HTTP_400_BAD_REQUEST
            )

        user = login.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})


class GetAllUserView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request: Request):
        users = CustomUser.objects.all()
        pages = self.paginate_queryset(users, request)
        users_serializers = CustomUserSerializer(pages, many=True)

        return self.get_paginated_response(users_serializers.data)


class UserProtectRouteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AcessOwnerOrAdmin]

    def get(self, request: Request, user_id):

        user = get_object_or_404(CustomUser, id=user_id)
        self.check_object_permissions(request, user)

        user_serializer = CustomUserSerializer(user)

        return Response(user_serializer.data)
