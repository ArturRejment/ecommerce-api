from abc import ABC

from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from .models import User


class UserCreateSerializer(UserCreateSerializer):

	class Meta(UserCreateSerializer.Meta):
		model = User
		fields = (
			'id',
			'email',
			'first_name',
			'last_name',
			'phone'
		)


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = (
			'id',
			'username',
			'email',
			'first_name',
			'last_name',
			'phone'
		)


class ChangePasswordSerializer(serializers.Serializer):
	model = User

	old_password = serializers.CharField(required=True)
	new_password = serializers.CharField(required=True)

