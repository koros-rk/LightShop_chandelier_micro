from rest_framework import serializers
from ..models import Color, ColorAvailability


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('title', 'hex')


class ColorAvailabilitySerializer(serializers.ModelSerializer):
    color = ColorSerializer()

    class Meta:
        model = ColorAvailability
        fields = ['color', 'availability', 'main_photo', 'price']
