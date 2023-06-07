from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Product
from ..serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all().filter(show=True)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        product_obj = Product.objects.filter(Q(category__title=instance.category.title)).exclude(pk=instance.pk).order_by('?')[:6]
        related = []
        for k in product_obj:
            ser = self.get_serializer(k)
            related.append(ser.data)
        related_data = serializer.data
        related_data["related"] = related
        return Response(related_data)

    @action(detail=False, methods=['GET'], url_path='slug/(?P<slug>[^/.]+)')
    def get_by_slug(self, request, slug=None):
        product = self.get_queryset().filter(slug=slug)
        serializer = self.get_serializer(product)

        product_obj = Product.objects.filter(Q(category__product__title__contains=product.category.title)).exclude(pk=product.pk).order_by('?')[:6]
        related = []
        for k in product_obj:
            ser = self.get_serializer(k)
            related.append(ser.data)
        related_data = serializer.data
        related_data["related"] = related

        return Response(related_data)
