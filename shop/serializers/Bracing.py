from rest_framework import serializers
from ..models import Bracing


class BracingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bracing
        fields = ('title',)
