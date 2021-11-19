from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):

	class Meta:
		model = Card
		fields = (
			'brand',
			'get_last_4',
			'owner_first_name',
			'owner_last_name',
		)