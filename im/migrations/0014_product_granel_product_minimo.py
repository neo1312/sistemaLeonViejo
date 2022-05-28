# Generated by Django 4.0.2 on 2022-03-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('im', '0013_product_margenmayoreo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='granel',
            field=models.BooleanField(default=False, verbose_name='granel'),
        ),
        migrations.AddField(
            model_name='product',
            name='minimo',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='minimo'),
        ),
    ]
