from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken, obtain_auth_token


urlpatterns = [
    path("users/register/", views.RegisterCustomView.as_view(), name="register"),
    path("users/login/", views.LoginWithObtainView.as_view(), name="login"),
    path("users/", views.GetAllUserView.as_view(), name="protected_routes"),
    path(
        "users/<int:user_id>",
        views.UserProtectRouteView.as_view(),
        name="protected_routes_id",
    ),
]

# EOF
