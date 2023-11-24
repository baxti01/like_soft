from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError
from rest_framework import serializers

User = get_user_model()


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'date_joined']
        read_only_fields = ['date_joined']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"},
        write_only=True
    )
    password_confirm = serializers.CharField(
        style={"input_type": "password"},
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'date_joined',
            'password', 'password_confirm'
        ]

    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.pop("password_confirm")

        if password != password_confirm:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        user = User(**attrs)

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user
