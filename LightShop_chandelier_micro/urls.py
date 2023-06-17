from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop.TelegramOrder import OrderView
from shop.viewsets import BracingViewSet, CategoryViewSet, ColorViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'bracings', BracingViewSet, basename='bracings')
router.register(r'colors', ColorViewSet, basename='colors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/order', OrderView.as_view()),
]
