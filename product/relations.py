from rest_framework import serializers

from .models import Category, Tag, Season


class CategoryRelatedField(serializers.RelatedField):

	def get_queryset(self):
		return Category.objects.all()

	def to_internal_value(self, data):
		category, created = Category.objects.get_or_create(category_name=data)

	def to_representation(self, value):
		return value.category_name


class TagRelatedField(serializers.RelatedField):

	def get_queryset(self):
		return Tag.objects.all()

	def to_internal_value(self, data):
		tag, created = Tag.objects.get_or_create(name=data)

	def to_representation(self, value):
		return value.name


class SeasonRelatedField(serializers.RelatedField):

	def get_queryset(self):
		return Season.objects.all()

	def to_internal_value(self, data):
		season, created = Season.objects.get_or_create(name=data)

	def to_representation(self, value):
		return value.name
