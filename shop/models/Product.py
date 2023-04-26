from django.db import models
from django.utils.text import slugify
from . import Color, Bracing, Category


class Product(models.Model):

    title = models.CharField(max_length=255, null=False, default='name')
    slug = models.SlugField(max_length=255, default='n')
    description = models.TextField(null=False, default='text')
    main_photo = models.URLField()
    base_price = models.IntegerField(null=False, default=1)
    plafod_count = models.IntegerField(null=True, default=1)
    potency = models.IntegerField(null=True, default=1)
    is_remote = models.BooleanField(null=False, default='false')
    is_led = models.BooleanField(null=False, default='false')

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    bracing = models.ForeignKey(Bracing, on_delete=models.PROTECT)
    colors = models.ManyToManyField(Color, through='ColorAvailability')

    availability = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ColorAvailability(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)

    availability = models.BooleanField(null=False, default='true')
    main_photo = models.URLField()
    price = models.IntegerField(null=False, default=1)
