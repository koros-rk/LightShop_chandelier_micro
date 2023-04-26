from rest_framework import serializers
from ..models import *
from . import BracingSerializer, CategorySerializer, ColorSerializer, ColorAvailabilitySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    bracing = BracingSerializer()
    colors = ColorAvailabilitySerializer(source='coloravailability_set', many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'description',
                  'main_photo', 'base_price', 'plafod_count',
                  'potency', 'is_remote', 'is_led',
                  'category', 'bracing', 'colors', 'time_created',
                  'time_updated', 'show', 'availability')
