from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from . import views

urlpatterns = [
    path("registration/", views.RegistrationApiView.as_view(), name="registration"),
    path("test-email/", views.TestEmailSend.as_view(), name="test_email"),
    path(
        "activation/confirm/<str:token>",
        views.ActivationApiView.as_view(),
        name="test_email",
    ),
    path(
        "activation/confirm/",
        views.ActivationResendApiView.as_view(),
        name="test_email",
    ),
    path(
        "password-change/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token-login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token-logout"),
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
]
