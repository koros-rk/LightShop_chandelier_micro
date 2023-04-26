from rest_framework import viewsets

from ..models import Color
from ..serializers import ColorSerializer


class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer

    def get_queryset(self):
        queryset = Color.objects.all()
        return queryset
