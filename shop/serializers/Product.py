from django.db.models import Q
from rest_framework import serializers
from ..models import *
from . import BracingSerializer, CategorySerializer, ColorSerializer, ColorAvailabilitySerializer
from rest_framework.response import Response


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

    def create(self, validated_data):
        colors_data = validated_data.pop('coloravailability_set')
        category_data = validated_data.pop('category')
        bracing_data = validated_data.pop('bracing')

        product = Product.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            main_photo=validated_data['main_photo'],
            base_price=validated_data['base_price'],
            plafod_count=validated_data['plafod_count'],
            potency=validated_data['potency'],
            is_remote=validated_data['is_remote'],
            is_led=validated_data['is_led'],
            show=validated_data['show'],
            availability=validated_data['availability'],
            bracing=Bracing.objects.get(**bracing_data),
            category=Category.objects.get(**category_data)
        )

        # category = Category.objects.create(**category_data)
        # product.category = category
        #
        # bracing = Bracing.objects.create(**bracing_data)
        # product.bracing = bracing

        for color_data in colors_data:
            color = Color.objects.get_or_create(**color_data['color'])[0]
            ColorAvailability.objects.create(product=product,
                                             color=color,
                                             main_photo=color_data['main_photo'],
                                             availability=color_data['availability'])

        product.save()

        return product

    def delete(self, instance):
        instance.delete()
