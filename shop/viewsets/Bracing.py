from rest_framework import viewsets

from ..models import Bracing
from ..serializers import BracingSerializer


class BracingViewSet(viewsets.ModelViewSet):
    serializer_class = BracingSerializer

    def get_queryset(self):
        queryset = Bracing.objects.all()
        return queryset
