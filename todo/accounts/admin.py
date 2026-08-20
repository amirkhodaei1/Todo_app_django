from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "is_superuser", "is_active","is_verified")
    list_filter = ("username", "is_superuser", "is_active","is_verified")
    search_fields = ("username",)
    ordering = ("username",)
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("username", "password"),
            },
        ),
        (
            "permmissions",
            {
                "fields": ("is_staff", "is_active", "is_superuser","is_verified"),
            },
        ),
        (
            "group permmissions",
            {
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "important date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_verified"
                    "is_superuser",
                ),
            },
        ),
    )