from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    readonly_fields = ["date_joined", "updated_at"]

    fieldsets = (
        ("Credentials", {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_critic", "is_superuser")}),
        (
            "Personal",
            {"fields": ("first_name", "last_name", "email", "birthdate", "bio")},
        ),
        ("Dates", {"fields": ("date_joined", "updated_at")}),
    )

    list_display = ("username", "is_superuser", "is_critic", "email")


admin.site.register(CustomUser, CustomUserAdmin)

#EOF