from django.test import TestCase
from rest_framework import status


class CategoryCRUDTestCase(TestCase):

    def test_get(self):
        responce = self.client.get("/api/v1/categories/")
        self.assertEqual(responce.status_code, status.HTTP_200_OK)


class BrasingCRUDTestCase(TestCase):
    def test_get(self):
        responce = self.client.get("/api/v1/bracings/")
        self.assertEqual(responce.status_code, status.HTTP_200_OK)


class ColorsCRUDTestCase(TestCase):
    def test_get(self):
        responce = self.client.get("/api/v1/colors/")
        self.assertEqual(responce.status_code, status.HTTP_200_OK)


class ProductsCRUDTestCase(TestCase):
    def test_get(self):
        responce = self.client.get("/api/v1/products/")
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
