# Generated by Django 4.2 on 2023-04-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_slug_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='plafod_count',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='potency',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
