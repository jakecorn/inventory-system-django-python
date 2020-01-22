# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-09-28 07:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_auto_20170928_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='product_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=5, validators=[django.core.validators.MaxValueValidator('errorrrorror')]),
        ),
    ]