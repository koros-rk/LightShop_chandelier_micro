from django.db import models


class Color(models.Model):
    title = models.CharField(max_length=250)
    hex = models.CharField(max_length=10)

    def __str__(self):
        return self.title
