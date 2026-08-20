from rest_framework import serializers
from ...models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError({"detail": "passwords not match"})
        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        return super().validate(attrs)

    def create(self, validate_data):
        validate_data.pop("password1", None)
        return User.objects.create_user(**validate_data)


class CustomAuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("username"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
            if user.is_verified:
                raise serializers.ValidationError({"detail": "user is not verified"})
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if self.user.is_verified:
            raise serializers.ValidationError({"detail": "user is not verified"})
        validated_data["username"] = self.user.username
        validated_data["user_id"] = self.user.id
        return validated_data


class ChangePasswordSerialier(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError({"detail": "passwords dosent match"})
        try:
            validate_password(attrs.get("new_password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"new_password": list(e.messages)})
        return super().validate(attrs)



class ActivationResendSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get("username")
        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "user dose not exist"})
        # if user_obj.is_verified:
        #     raise serializers.ValidationError({"detail": "user is already activated"})
        attrs['user']=user_obj
        return super().validate(attrs)
